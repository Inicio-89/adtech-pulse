# database.py — SQLite database setup and queries
# =================================================
# This file handles ALL database operations.
# SQLite comes built into Python — no installation needed.
# The database is just a single file (adtech_pulse.db) on your computer.
#
# KEY CONCEPTS:
# - A "table" is like a spreadsheet tab (we have one called "articles")
# - Each "row" is one article/episode
# - Each "column" is a piece of info (title, link, date, etc.)
# - SQL is the language used to talk to the database

import sqlite3
from datetime import datetime


# --- DATABASE FILE PATH ---
DB_PATH = "adtech_pulse.db"


def get_connection():
    """
    Opens a connection to the database.
    If the database file doesn't exist yet, SQLite creates it automatically.
    
    Think of this like opening a spreadsheet file — you need to open it
    before you can read or write data.
    """
    conn = sqlite3.connect(DB_PATH)
    # This line makes query results return as dictionaries instead of tuples
    # So you can access data like row["title"] instead of row[0]
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    """
    Creates the database tables if they don't exist yet.
    Run this once when you first start the app.
    
    SQL BREAKDOWN:
    - CREATE TABLE IF NOT EXISTS = make a new table (skip if it already exists)
    - TEXT = a column that holds text/strings
    - INTEGER = a column that holds numbers
    - PRIMARY KEY = unique ID for each row (auto-increments)
    - UNIQUE = no two rows can have the same value in this column
    """
    conn = get_connection()
    cursor = conn.cursor()

    # --- ARTICLES TABLE ---
    # Stores both news articles AND podcast episodes
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS articles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            link TEXT UNIQUE NOT NULL,
            description TEXT,
            source_name TEXT,
            source_type TEXT DEFAULT 'news',
            category TEXT DEFAULT 'general',
            published_date TEXT,
            fetched_date TEXT,
            audio_url TEXT,
            audio_duration TEXT,
            sentiment_score REAL DEFAULT 0.0,
            is_trending INTEGER DEFAULT 0
        )
    """)

    # --- INDEX FOR FASTER SEARCHES ---
    # An index is like a table of contents — helps find things faster
    cursor.execute("""
        CREATE INDEX IF NOT EXISTS idx_published 
        ON articles(published_date DESC)
    """)
    cursor.execute("""
        CREATE INDEX IF NOT EXISTS idx_category 
        ON articles(category)
    """)
    cursor.execute("""
        CREATE INDEX IF NOT EXISTS idx_source_type 
        ON articles(source_type)
    """)

    conn.commit()  # Save changes
    conn.close()   # Close the connection
    print("Database initialized successfully!")


def save_article(article_data):
    """
    Saves a single article to the database.
    If the article already exists (same link), it skips it.
    
    Parameters:
        article_data (dict): A dictionary with article info like:
            {
                "title": "New Privacy Rules...",
                "link": "https://...",
                "description": "Article summary...",
                "source_name": "AdExchanger",
                "source_type": "news",
                "category": "privacy",
                "published_date": "2026-02-16",
                "audio_url": None,
                "audio_duration": None
            }
    
    Returns:
        bool: True if saved, False if it already existed
    """
    conn = get_connection()
    cursor = conn.cursor()

    try:
        # INSERT OR IGNORE = try to add it, but if the link already exists, skip it
        cursor.execute("""
            INSERT OR IGNORE INTO articles 
            (title, link, description, source_name, source_type, category, 
             published_date, fetched_date, audio_url, audio_duration)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            article_data.get("title", ""),
            article_data.get("link", ""),
            article_data.get("description", ""),
            article_data.get("source_name", ""),
            article_data.get("source_type", "news"),
            article_data.get("category", "general"),
            article_data.get("published_date", ""),
            datetime.now().isoformat(),
            article_data.get("audio_url"),
            article_data.get("audio_duration"),
        ))
        conn.commit()
        # rowcount tells us if a row was actually inserted (1) or skipped (0)
        saved = cursor.rowcount > 0
        return saved

    except Exception as e:
        print(f"Error saving article: {e}")
        return False

    finally:
        conn.close()


def get_latest_articles(limit=20, source_type=None, category=None):
    """
    Gets the most recent articles from the database.
    
    Parameters:
        limit (int): How many articles to return (default 20)
        source_type (str): Filter by 'news' or 'podcast' (optional)
        category (str): Filter by category like 'privacy' (optional)
    
    Returns:
        list: A list of article dictionaries
    
    SQL BREAKDOWN:
    - SELECT * = get all columns
    - FROM articles = from the articles table
    - WHERE = filter conditions
    - ORDER BY = sort results (DESC = newest first)
    - LIMIT = only return this many results
    """
    conn = get_connection()
    cursor = conn.cursor()

    # Build the query dynamically based on filters
    query = "SELECT * FROM articles WHERE 1=1"
    params = []

    if source_type:
        query += " AND source_type = ?"
        params.append(source_type)

    if category:
        query += " AND category = ?"
        params.append(category)

    query += " ORDER BY published_date DESC LIMIT ?"
    params.append(limit)

    cursor.execute(query, params)
    articles = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return articles


def search_articles(search_term, limit=20):
    """
    Searches articles by title or description.
    
    The LIKE operator with % wildcards means "contains this text anywhere"
    So '%privacy%' matches "New privacy rules" and "The future of privacy"
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM articles 
        WHERE title LIKE ? OR description LIKE ?
        ORDER BY published_date DESC 
        LIMIT ?
    """, (f"%{search_term}%", f"%{search_term}%", limit))

    articles = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return articles


def get_article_count():
    """Returns the total number of articles in the database."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) as count FROM articles")
    result = cursor.fetchone()
    conn.close()
    return result["count"]


def get_articles_by_date_range(start_date, end_date):
    """
    Gets articles within a date range — useful for the trends dashboard.
    Dates should be in 'YYYY-MM-DD' format.
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM articles 
        WHERE published_date BETWEEN ? AND ?
        ORDER BY published_date DESC
    """, (start_date, end_date))

    articles = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return articles


def get_category_counts():
    """
    Returns how many articles are in each category.
    Useful for the sidebar/navigation showing article counts.
    
    GROUP BY = groups rows with the same category together
    COUNT(*) = counts how many are in each group
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT category, COUNT(*) as count 
        FROM articles 
        GROUP BY category 
        ORDER BY count DESC
    """)

    counts = {row["category"]: row["count"] for row in cursor.fetchall()}
    conn.close()
    return counts


def get_source_counts():
    """Returns how many articles came from each source."""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT source_name, COUNT(*) as count 
        FROM articles 
        GROUP BY source_name 
        ORDER BY count DESC
    """)

    counts = {row["source_name"]: row["count"] for row in cursor.fetchall()}
    conn.close()
    return counts
