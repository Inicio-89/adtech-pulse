# feed_parser.py — RSS Feed Fetching and Processing
# ===================================================
# This is the ENGINE of AdTech Pulse.
# It goes out to the internet, grabs RSS feeds from ad industry sites,
# parses the content, categorizes it, and saves it to the database.
#
# UPDATED: Now uses ALL_FEEDS from config.py which combines news, podcasts,
# Reddit, Bluesky, Mastodon, Hacker News, and Substack into one list.
# Each feed has a content_type field so we know where it came from.
#
# KEY CONCEPTS:
# - RSS = Really Simple Syndication — a standard format websites use to publish updates
# - An RSS feed is just an XML file with article titles, descriptions, dates, and links
# - feedparser is a Python library that reads these XML files and gives us clean data
# - We run this periodically (every hour) to keep content fresh

import feedparser
import re
import socket
socket.setdefaulttimeout(15)
from datetime import datetime
from database import save_article
from config import ALL_FEEDS, NEWS_FEEDS, PODCAST_FEEDS, CATEGORIES


# =============================================
# CUSTOM USER-AGENT
# =============================================
# Reddit blocks the default Python user-agent.
# Some other sites may also throttle or block generic requests.
# This identifies us as a legitimate feed reader.
USER_AGENT = "AdTechPulse/1.0 (RSS Aggregator; +https://github.com/Inicio-89/adtech-pulse)"


def categorize_article(title, description):
    """
    Automatically assigns a category to an article based on keywords.
    
    HOW IT WORKS:
    1. Combine the title and description into one big string
    2. Convert to lowercase (so "Privacy" matches "privacy")
    3. Check each category's keywords against the text
    4. Count how many keyword matches each category gets
    5. The category with the most matches wins
    
    If no keywords match, it defaults to "general"
    """
    text = f"{title or ''} {description or ''}".lower()

    best_category = "general"
    best_score = 0

    for category_key, category_info in CATEGORIES.items():
        score = 0
        for keyword in category_info["keywords"]:
            if keyword.lower() in text:
                score += 1

        if score > best_score:
            best_score = score
            best_category = category_key

    return best_category


def parse_date(entry):
    """
    Extracts and normalizes the publication date from a feed entry.
    RSS feeds store dates in various formats. This handles the mess.
    """
    try:
        if hasattr(entry, 'published_parsed') and entry.published_parsed:
            dt = datetime(*entry.published_parsed[:6])
            return dt.strftime("%Y-%m-%d %H:%M:%S")
        elif hasattr(entry, 'updated_parsed') and entry.updated_parsed:
            dt = datetime(*entry.updated_parsed[:6])
            return dt.strftime("%Y-%m-%d %H:%M:%S")
        elif hasattr(entry, 'published') and entry.published:
            return entry.published
    except Exception:
        pass

    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def clean_html(text):
    """
    Removes HTML tags from text.
    RSS descriptions often contain HTML like <p>, <a>, <img> tags.
    We want plain text for display and analysis.
    """
    if not text:
        return ""

    # Remove HTML tags
    clean = re.sub(r'<[^>]+>', '', text)
    # Remove extra whitespace
    clean = re.sub(r'\s+', ' ', clean).strip()
    # Decode common HTML entities
    clean = clean.replace('&amp;', '&')
    clean = clean.replace('&lt;', '<')
    clean = clean.replace('&gt;', '>')
    clean = clean.replace('&quot;', '"')
    clean = clean.replace('&#39;', "'")
    clean = clean.replace('&nbsp;', ' ')

    # Truncate very long descriptions
    if len(clean) > 500:
        clean = clean[:497] + "..."

    return clean


def fetch_feed(feed_info):
    """
    Fetches a single feed and returns a list of article dicts ready for saving.
    
    This is the unified fetch function that handles ALL feed types:
    news, podcast, reddit, bluesky, mastodon, hackernews, substack.
    
    The content_type from config.py tells us what kind of source it is,
    which helps the UI display it differently (e.g., label Reddit posts
    as "Community" rather than "News").
    
    Parameters:
        feed_info (dict): Feed configuration from config.py with keys:
            name, url, category, content_type
    
    Returns:
        tuple: (articles_list, stats_dict)
    """
    feed_name = feed_info["name"]
    feed_url = feed_info["url"]
    default_category = feed_info.get("category", "general")
    content_type = feed_info.get("content_type", "news")
    
    articles = []
    
    try:
        # feedparser.parse() does the heavy lifting:
        # - Makes an HTTP request to the URL
        # - Downloads the XML content
        # - Parses it into a Python object with .entries, .feed, etc.
        #
        # We pass a custom user-agent because Reddit (and some other sites)
        # block requests from the default Python user-agent.
        feed = feedparser.parse(
            feed_url,
            agent=USER_AGENT
        )

        if feed.bozo and not feed.entries:
            print(f"  WARNING: Feed error for {feed_name} — skipping")
            return [], {"fetched": 0, "errors": 1}

        for entry in feed.entries:
            # Extract core data from the feed entry
            title = entry.get("title", "").strip()
            link = entry.get("link", "").strip()
            description = clean_html(
                entry.get("summary", "") or entry.get("description", "")
            )

            # Skip entries without a title or link
            if not title or not link:
                continue

            # Auto-categorize based on content keywords
            category = categorize_article(title, description)
            if category == "general":
                category = default_category

            # Build the article data dictionary
            article_data = {
                "title": title,
                "link": link,
                "description": description,
                "source_name": feed_name,
                "source_type": content_type,  # <-- This is the key change
                "category": category,
                "published_date": parse_date(entry),
            }

            # Podcast-specific: extract audio URL and duration
            if content_type == "podcast":
                audio_url = None
                if hasattr(entry, 'enclosures') and entry.enclosures:
                    audio_url = entry.enclosures[0].get("href", "")
                article_data["audio_url"] = audio_url
                article_data["audio_duration"] = entry.get("itunes_duration", "")

            articles.append(article_data)
        
        return articles, {"fetched": len(articles), "errors": 0}

    except Exception as e:
        print(f"  ERROR fetching {feed_name}: {e}")
        return [], {"fetched": 0, "errors": 1}


def fetch_all_feeds():
    """
    Master function — fetches ALL feeds from config.py's ALL_FEEDS list.
    
    This replaces the old separate fetch_news_feeds() and fetch_podcast_feeds().
    Now it loops through every feed in ALL_FEEDS (news, podcasts, reddit,
    bluesky, mastodon, hackernews, substack) in one pass.
    """
    total_fetched = 0
    total_saved = 0
    total_errors = 0
    source_count = len(ALL_FEEDS)

    print(f"\n{'='*60}")
    print(f"Fetching {source_count} feeds at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'='*60}")

    # Group feeds by content_type for cleaner logging
    feed_types = {}
    for feed in ALL_FEEDS:
        ct = feed.get("content_type", "news")
        feed_types.setdefault(ct, []).append(feed)

    for content_type, feeds in feed_types.items():
        print(f"\n--- {content_type.upper()} ({len(feeds)} sources) ---")
        
        for feed_info in feeds:
            feed_name = feed_info["name"]
            print(f"  Fetching: {feed_name}...", end=" ")
            
            articles, stats = fetch_feed(feed_info)
            total_fetched += stats["fetched"]
            total_errors += stats["errors"]
            
            if stats["errors"]:
                continue
            
            # Save each article to database
            saved_count = 0
            for article_data in articles:
                if save_article(article_data):
                    saved_count += 1
            
            total_saved += saved_count
            print(f"found {stats['fetched']}, saved {saved_count} new")

    print(f"\n{'='*60}")
    print(f"Fetch complete: {total_fetched} checked, {total_saved} new saved, {total_errors} errors")
    print(f"{'='*60}")

    return {
        "total_fetched": total_fetched,
        "new_saved": total_saved,
        "sources_checked": source_count,
        "errors": total_errors,
    }


# =============================================
# BACKWARD COMPATIBILITY
# =============================================
# These functions still work if app.py calls them by the old names.
# They just delegate to the unified fetch_all_feeds().

def fetch_news_feeds():
    """Legacy wrapper — fetches only news feeds."""
    total_fetched = 0
    new_saved = 0
    for feed_info in NEWS_FEEDS:
        fi = dict(feed_info, content_type="news")
        articles, stats = fetch_feed(fi)
        total_fetched += stats["fetched"]
        for a in articles:
            if save_article(a):
                new_saved += 1
    return {"total_fetched": total_fetched, "new_saved": new_saved, "sources_checked": len(NEWS_FEEDS)}


def fetch_podcast_feeds():
    """Legacy wrapper — fetches only podcast feeds."""
    total_fetched = 0
    new_saved = 0
    for feed_info in PODCAST_FEEDS:
        fi = dict(feed_info, content_type="podcast")
        articles, stats = fetch_feed(fi)
        total_fetched += stats["fetched"]
        for a in articles:
            if save_article(a):
                new_saved += 1
    return {"total_fetched": total_fetched, "new_saved": new_saved, "sources_checked": len(PODCAST_FEEDS)}


# --- RUN DIRECTLY ---
# If you run this file by itself (python feed_parser.py), it fetches ALL feeds
if __name__ == "__main__":
    print("Starting manual feed fetch...")
    result = fetch_all_feeds()
    print(f"\nDone! Total new content saved: {result['new_saved']}")
