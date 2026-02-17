# app.py — Main Flask Application
# ==================================
# This is the HEART of AdTech Pulse.
# Flask is a Python web framework — it turns your Python code into a website.
#
# KEY CONCEPTS:
# - A "route" maps a URL to a Python function
#   Example: @app.route('/') means "when someone visits the homepage, run this function"
# - render_template() takes an HTML file and fills in data from Python
# - The templates/ folder holds HTML files
# - The static/ folder holds CSS, JavaScript, and images
#
# TO RUN THIS APP:
# 1. Install dependencies: pip install flask feedparser
# 2. Run: python app.py
# 3. Open browser: http://localhost:5000

from flask import Flask, render_template, request
from database import (
    init_db, get_latest_articles, search_articles,
    get_article_count, get_category_counts, get_source_counts
)
from feed_parser import fetch_all_feeds
from config import APP_NAME, APP_TAGLINE, CATEGORIES, DEBUG

# --- CREATE THE FLASK APP ---
# This creates the application object that handles all web requests
app = Flask(__name__)


# --- CONTEXT PROCESSOR ---
# This makes certain variables available in ALL templates automatically
# So you don't have to pass APP_NAME to every single render_template() call
@app.context_processor
def inject_globals():
    return {
        "app_name": APP_NAME,
        "app_tagline": APP_TAGLINE,
        "categories": CATEGORIES,
        "category_counts": get_category_counts(),
    }


# ============================================================
# ROUTES — Each one maps a URL to a page
# ============================================================

@app.route("/")
def index():
    """
    HOMEPAGE — shows the latest articles across all sources.
    
    URL: http://localhost:5000/
    
    What happens:
    1. Get the 20 most recent news articles from the database
    2. Get the 5 most recent podcast episodes
    3. Pass them to the index.html template
    4. Flask renders the HTML and sends it to the browser
    """
    news = get_latest_articles(limit=20, source_type="news")
    podcasts = get_latest_articles(limit=5, source_type="podcast")
    total_articles = get_article_count()

    return render_template(
        "index.html",
        news=news,
        podcasts=podcasts,
        total_articles=total_articles,
        page_title="Home"
    )


@app.route("/category/<category_name>")
def category(category_name):
    """
    CATEGORY PAGE — shows articles filtered by topic.
    
    URL: http://localhost:5000/category/privacy
    URL: http://localhost:5000/category/programmatic
    
    The <category_name> part of the URL becomes a Python variable.
    So visiting /category/privacy sets category_name = "privacy"
    """
    # Look up the display name (e.g., "privacy" → "Privacy & Data")
    category_info = CATEGORIES.get(category_name, {})
    display_name = category_info.get("display_name", category_name.title())

    articles = get_latest_articles(limit=30, category=category_name)

    return render_template(
        "category.html",
        articles=articles,
        category_name=category_name,
        display_name=display_name,
        page_title=display_name,
    )


@app.route("/podcasts")
def podcasts():
    """
    PODCASTS PAGE — shows all podcast episodes.
    
    URL: http://localhost:5000/podcasts
    """
    episodes = get_latest_articles(limit=30, source_type="podcast")

    return render_template(
        "podcasts.html",
        episodes=episodes,
        page_title="Podcasts",
    )


@app.route("/search")
def search():
    """
    SEARCH PAGE — searches articles by keyword.
    
    URL: http://localhost:5000/search?q=privacy
    
    request.args.get("q") gets the search term from the URL.
    The ?q=privacy part is called a "query parameter."
    """
    query = request.args.get("q", "").strip()
    results = []

    if query:
        results = search_articles(query, limit=30)

    return render_template(
        "search.html",
        query=query,
        results=results,
        page_title=f"Search: {query}" if query else "Search",
    )


@app.route("/about")
def about():
    """
    ABOUT PAGE — info about the site.
    
    URL: http://localhost:5000/about
    """
    source_counts = get_source_counts()
    total = get_article_count()

    return render_template(
        "about.html",
        source_counts=source_counts,
        total_articles=total,
        page_title="About",
    )


@app.route("/refresh")
def refresh_feeds():
    """
    MANUAL REFRESH — triggers a feed fetch.
    
    URL: http://localhost:5000/refresh
    
    In production, you'd run this on a schedule (cron job or APScheduler).
    This route lets you trigger it manually for testing.
    """
    result = fetch_all_feeds()

    return render_template(
        "refresh.html",
        result=result,
        page_title="Feed Refresh",
    )


# ============================================================
# START THE APP
# ============================================================

if __name__ == "__main__":
    # Initialize the database (creates tables if they don't exist)
    init_db()

    # Fetch feeds on startup so you have content immediately
    print("Fetching initial content...")
    fetch_all_feeds()

    # Start the web server
    # debug=True means it auto-reloads when you change code
    # host="0.0.0.0" makes it accessible on your network
    print(f"\n{'='*50}")
    print(f"{APP_NAME} is running!")
    print(f"Open http://localhost:5000 in your browser")
    print(f"{'='*50}\n")

    app.run(debug=DEBUG, host="0.0.0.0", port=5000)
