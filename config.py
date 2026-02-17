# config.py — Feed URLs and application settings
# ================================================
# This file stores all the configuration for AdTech Pulse.
# When you want to add a new feed source, just add it to the appropriate list below.

# --- APPLICATION SETTINGS ---
APP_NAME = "AdTech Pulse"
APP_TAGLINE = "Your daily dose of advertising industry intelligence"
DEBUG = True  # Set to False when deploying to production

# --- HOW OFTEN TO PULL FEEDS (in minutes) ---
FETCH_INTERVAL = 60  # Pull new content every 60 minutes

# --- NEWS RSS FEEDS ---
# Each feed has a name (what you see on the site) and a URL (where Python fetches from)
# To add a new source: just add another dictionary to this list
NEWS_FEEDS = [
    {
        "name": "AdExchanger",
        "url": "https://www.adexchanger.com/feed/",
        "category": "programmatic"
    },
    {
        "name": "Digiday",
        "url": "https://digiday.com/feed/",
        "category": "media"
    },
    {
        "name": "AdWeek",
        "url": "https://www.adweek.com/feed/",
        "category": "advertising"
    },
    {
        "name": "AdTech Daily",
        "url": "https://adtechdaily.com/feed",
        "category": "adtech"
    },
    {
        "name": "VideoWeek",
        "url": "https://videoweek.com/feed",
        "category": "ctv"
    },
]

# --- PODCAST RSS FEEDS ---
# Podcast feeds work the same as news feeds but include audio enclosures
PODCAST_FEEDS = [
    {
        "name": "AdExchanger Talks",
        "url": "https://feeds.megaphone.fm/adexchanger",
        "category": "programmatic"
    },
    {
        "name": "AdTechGod Pod",
        "url": "https://feeds.buzzsprout.com/2057436.rss",
        "category": "adtech"
    },
]

# --- CATEGORIES ---
# These are the topic categories for organizing content
# The keywords help auto-tag articles into the right category
CATEGORIES = {
    "programmatic": {
        "display_name": "Programmatic",
        "keywords": ["programmatic", "dsp", "ssp", "rtb", "real-time bidding", "auction",
                     "bid", "impression", "exchange", "demand-side", "supply-side"]
    },
    "measurement": {
        "display_name": "Measurement",
        "keywords": ["measurement", "attribution", "brand lift", "viewability", "roi",
                     "analytics", "kpi", "conversion", "incrementality", "survey"]
    },
    "privacy": {
        "display_name": "Privacy & Data",
        "keywords": ["privacy", "gdpr", "ccpa", "cookie", "cookieless", "consent",
                     "first-party", "third-party", "identity", "tracking"]
    },
    "ctv": {
        "display_name": "CTV & Video",
        "keywords": ["ctv", "connected tv", "ott", "streaming", "video", "television",
                     "linear", "cord-cutting", "avod", "fast"]
    },
    "media": {
        "display_name": "Media & Publishing",
        "keywords": ["publisher", "media", "content", "editorial", "subscription",
                     "paywall", "audience", "reach", "engagement"]
    },
    "advertising": {
        "display_name": "Advertising & Creative",
        "keywords": ["creative", "campaign", "brand", "agency", "ad spend", "budget",
                     "advertiser", "marketing", "strategy"]
    },
    "adtech": {
        "display_name": "Ad Tech",
        "keywords": ["ad tech", "adtech", "platform", "technology", "api", "integration",
                     "saas", "automation", "ai", "machine learning"]
    },
}

# --- STOP WORDS ---
# Common words to ignore when analyzing trending topics
STOP_WORDS = {
    "the", "a", "an", "and", "or", "but", "in", "on", "at", "to", "for", "of", "with",
    "by", "from", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had",
    "do", "does", "did", "will", "would", "could", "should", "may", "might", "can",
    "this", "that", "these", "those", "it", "its", "not", "no", "how", "what", "which",
    "who", "whom", "when", "where", "why", "all", "each", "every", "both", "few", "more",
    "most", "other", "some", "such", "than", "too", "very", "just", "about", "above",
    "after", "again", "also", "as", "new", "said", "says", "according", "via", "into",
    "over", "up", "out", "so", "if", "then", "now", "here", "there", "they", "them",
    "their", "our", "we", "us", "you", "your", "he", "she", "his", "her", "my", "me",
}
