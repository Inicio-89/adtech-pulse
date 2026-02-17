# feed_parser.py — RSS Feed Fetching and Processing
# ===================================================
# This is the ENGINE of AdTech Pulse.
# It goes out to the internet, grabs RSS feeds from ad industry sites,
# parses the content, categorizes it, and saves it to the database.
#
# KEY CONCEPTS:
# - RSS = Really Simple Syndication — a standard format websites use to publish updates
# - An RSS feed is just an XML file with article titles, descriptions, dates, and links
# - feedparser is a Python library that reads these XML files and gives us clean data
# - We run this periodically (every hour) to keep content fresh

import feedparser
from datetime import datetime
from database import save_article
from config import NEWS_FEEDS, PODCAST_FEEDS, CATEGORIES


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
    
    Parameters:
        title (str): Article headline
        description (str): Article summary/body
    
    Returns:
        str: Category key like "privacy" or "programmatic"
    """
    # Combine title and description, handle None values
    text = f"{title or ''} {description or ''}".lower()

    best_category = "general"
    best_score = 0

    # Check each category's keywords
    for category_key, category_info in CATEGORIES.items():
        score = 0
        for keyword in category_info["keywords"]:
            if keyword.lower() in text:
                score += 1

        # If this category has more keyword matches, it wins
        if score > best_score:
            best_score = score
            best_category = category_key

    return best_category


def parse_date(entry):
    """
    Extracts and normalizes the publication date from a feed entry.
    
    RSS feeds store dates in various formats. feedparser tries to parse them
    into a consistent format, but sometimes fails. This function handles that.
    
    Parameters:
        entry: A feedparser entry object
    
    Returns:
        str: Date in 'YYYY-MM-DD HH:MM:SS' format, or current time if parsing fails
    """
    try:
        # feedparser provides a parsed date tuple in 'published_parsed'
        if hasattr(entry, 'published_parsed') and entry.published_parsed:
            dt = datetime(*entry.published_parsed[:6])
            return dt.strftime("%Y-%m-%d %H:%M:%S")
        # Fallback: try the raw published string
        elif hasattr(entry, 'published') and entry.published:
            return entry.published
    except Exception:
        pass

    # If all else fails, use current time
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def clean_html(text):
    """
    Removes HTML tags from text.
    RSS descriptions often contain HTML like <p>, <a>, <img> tags.
    We want plain text for display and analysis.
    
    This is a simple approach — for production you might use BeautifulSoup,
    but this works fine for our needs.
    """
    if not text:
        return ""

    import re
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


def fetch_news_feeds():
    """
    Fetches all news RSS feeds and saves new articles to the database.
    
    WHAT HAPPENS:
    1. Loop through each feed URL in config.py
    2. feedparser fetches and parses the RSS XML
    3. For each article in the feed, extract title, link, description, date
    4. Auto-categorize the article based on keywords
    5. Save to database (skips duplicates automatically)
    
    Returns:
        dict: Summary of what was fetched
            {"total_fetched": 45, "new_saved": 12, "sources_checked": 5}
    """
    total_fetched = 0
    new_saved = 0

    print(f"\n{'='*50}")
    print(f"Fetching news feeds at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'='*50}")

    for feed_info in NEWS_FEEDS:
        feed_name = feed_info["name"]
        feed_url = feed_info["url"]
        default_category = feed_info.get("category", "general")

        print(f"\nFetching: {feed_name}...")

        try:
            # feedparser.parse() does the heavy lifting:
            # - Makes an HTTP request to the URL
            # - Downloads the XML content
            # - Parses it into a Python object with .entries, .feed, etc.
            feed = feedparser.parse(feed_url)

            if feed.bozo and not feed.entries:
                # 'bozo' means the feed had errors; if no entries, skip it
                print(f"  WARNING: Feed error for {feed_name} — skipping")
                continue

            entry_count = len(feed.entries)
            print(f"  Found {entry_count} entries")

            for entry in feed.entries:
                total_fetched += 1

                # Extract data from the feed entry
                title = entry.get("title", "").strip()
                link = entry.get("link", "").strip()
                description = clean_html(
                    entry.get("summary", "") or entry.get("description", "")
                )

                # Skip entries without a title or link
                if not title or not link:
                    continue

                # Auto-categorize based on content
                category = categorize_article(title, description)
                # If auto-categorization returns "general", use the feed's default
                if category == "general":
                    category = default_category

                # Build the article data dictionary
                article_data = {
                    "title": title,
                    "link": link,
                    "description": description,
                    "source_name": feed_name,
                    "source_type": "news",
                    "category": category,
                    "published_date": parse_date(entry),
                }

                # Save to database (returns True if new, False if duplicate)
                if save_article(article_data):
                    new_saved += 1

        except Exception as e:
            print(f"  ERROR fetching {feed_name}: {e}")

    print(f"\n{'='*50}")
    print(f"News fetch complete: {total_fetched} checked, {new_saved} new articles saved")
    print(f"{'='*50}")

    return {
        "total_fetched": total_fetched,
        "new_saved": new_saved,
        "sources_checked": len(NEWS_FEEDS),
    }


def fetch_podcast_feeds():
    """
    Fetches podcast RSS feeds and saves episodes to the database.
    
    Podcast feeds are similar to news feeds but include audio information:
    - enclosures: contain the audio file URL and duration
    - itunes tags: contain episode duration, episode number, etc.
    """
    total_fetched = 0
    new_saved = 0

    print(f"\nFetching podcast feeds...")

    for feed_info in PODCAST_FEEDS:
        feed_name = feed_info["name"]
        feed_url = feed_info["url"]
        default_category = feed_info.get("category", "general")

        print(f"\nFetching podcast: {feed_name}...")

        try:
            feed = feedparser.parse(feed_url)

            if feed.bozo and not feed.entries:
                print(f"  WARNING: Feed error for {feed_name} — skipping")
                continue

            print(f"  Found {len(feed.entries)} episodes")

            for entry in feed.entries:
                total_fetched += 1

                title = entry.get("title", "").strip()
                link = entry.get("link", "").strip()
                description = clean_html(
                    entry.get("summary", "") or entry.get("description", "")
                )

                if not title or not link:
                    continue

                # Extract audio URL from enclosures
                audio_url = None
                if hasattr(entry, 'enclosures') and entry.enclosures:
                    audio_url = entry.enclosures[0].get("href", "")

                # Extract duration (podcasts often have itunes_duration)
                audio_duration = entry.get("itunes_duration", "")

                category = categorize_article(title, description)
                if category == "general":
                    category = default_category

                article_data = {
                    "title": title,
                    "link": link,
                    "description": description,
                    "source_name": feed_name,
                    "source_type": "podcast",
                    "category": category,
                    "published_date": parse_date(entry),
                    "audio_url": audio_url,
                    "audio_duration": audio_duration,
                }

                if save_article(article_data):
                    new_saved += 1

        except Exception as e:
            print(f"  ERROR fetching {feed_name}: {e}")

    print(f"Podcast fetch complete: {total_fetched} checked, {new_saved} new saved")

    return {
        "total_fetched": total_fetched,
        "new_saved": new_saved,
        "sources_checked": len(PODCAST_FEEDS),
    }


def fetch_all_feeds():
    """
    Master function — fetches both news and podcast feeds.
    Call this on a schedule to keep the site updated.
    """
    news_result = fetch_news_feeds()
    podcast_result = fetch_podcast_feeds()

    return {
        "news": news_result,
        "podcasts": podcast_result,
        "total_new": news_result["new_saved"] + podcast_result["new_saved"],
    }


# --- RUN DIRECTLY ---
# If you run this file by itself (python feed_parser.py), it fetches all feeds
if __name__ == "__main__":
    print("Starting manual feed fetch...")
    result = fetch_all_feeds()
    print(f"\nDone! Total new content saved: {result['total_new']}")
