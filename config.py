# config.py — Feed URLs and application settings
# ================================================
# AdTech Pulse (working title) — Complete Feed Configuration
# Last updated: February 18, 2026
#
# FEED TIERS:
#   Tier 1 = Core industry news (high volume, high signal)
#   Tier 2 = Vendor/platform blogs (prospect research + product launches)
#   Tier 3 = Niche verticals (retail media, measurement)
#
# SOCIAL/COMMUNITY FEEDS:
#   Reddit = Unfiltered practitioner opinions, real questions
#   Bluesky = Real-time industry reaction, hot takes from key voices
#   Mastodon = Privacy/open-web crowd, technical ad tech discussion
#   Hacker News = Tech-forward perspective on ad tech
#   Substack = Deep-dive analysis from independent writers

# --- APPLICATION SETTINGS ---
APP_NAME = "AdTech Pulse"
APP_TAGLINE = "Your daily dose of advertising industry intelligence"
DEBUG = True  # Set to False when deploying to production

# --- HOW OFTEN TO PULL FEEDS (in minutes) ---
FETCH_INTERVAL = 60  # Pull new content every 60 minutes

# --- ARTICLE RETENTION ---
RETENTION_DAYS = 7  # Keep articles for 7 days minimum for trend analysis


# =============================================================
# NEWS RSS FEEDS (24 sources)
# =============================================================
NEWS_FEEDS = [
    # =====================
    # TIER 1 — Core Industry News (9 sources)
    # =====================
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
        "name": "AdWeek Ad Tech",
        "url": "https://adweek.com/category/ad-tech/feed",
        "category": "adtech"
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
    {
        "name": "ExchangeWire",
        "url": "https://feeds.feedburner.com/Exchangewirecom",
        "category": "adtech"
    },
    {
        "name": "Marketing Dive — MarTech",
        "url": "https://marketingdive.com/topic/marketing-technology/feed",
        "category": "adtech"
    },
    {
        "name": "TechCrunch Ad Tech",
        "url": "https://techcrunch.com/tag/advertising-tech/feed",
        "category": "adtech"
    },

    # =====================
    # TIER 2 — Vendor & Platform Blogs (10 sources)
    # Great for understanding prospect companies
    # =====================
    {
        "name": "Basis Technologies",
        "url": "https://basis.com/blog/feed",
        "category": "programmatic"
    },
    {
        "name": "Clearcode",
        "url": "https://clearcode.cc/feed",
        "category": "adtech"
    },
    {
        "name": "OpenX",
        "url": "https://blog.openx.com/feed",
        "category": "programmatic"
    },
    {
        "name": "Magnite",
        "url": "https://magnite.com/blog/feed",
        "category": "ctv"
    },
    {
        "name": "Index Exchange",
        "url": "https://indexexchange.com/blog/feed",
        "category": "programmatic"
    },
    {
        "name": "Prebid",
        "url": "https://prebid.org/feed",
        "category": "programmatic"
    },
    {
        "name": "Equativ",
        "url": "https://equativ.com/feed",
        "category": "programmatic"
    },
    {
        "name": "MNTN",
        "url": "https://mountain.com/blog/feed",
        "category": "ctv"
    },
    {
        "name": "MediaRadar",
        "url": "https://mediaradar.com/blog/rss.xml",
        "category": "measurement"
    },
    {
        "name": "Verve Group",
        "url": "https://verve.com/feed",
        "category": "privacy"
    },

    # =====================
    # TIER 3 — Retail Media & Niche (5 sources)
    # =====================
    {
        "name": "Retail TouchPoints",
        "url": "https://retailtouchpoints.com/feed",
        "category": "retail_media"
    },
    {
        "name": "Tinuiti",
        "url": "https://tinuiti.com/feed",
        "category": "retail_media"
    },
    {
        "name": "More About Advertising",
        "url": "https://moreaboutadvertising.com/feed",
        "category": "advertising"
    },
    {
        "name": "Adtech Today",
        "url": "https://adtechtoday.com/feed",
        "category": "adtech"
    },
]


# =============================================================
# PODCAST RSS FEEDS (8 sources)
# =============================================================
PODCAST_FEEDS = [
    # =====================
    # TIER 1 — Must-Listen for Ad Tech (5 sources)
    # =====================
    {
        "name": "AdExchanger Talks",
        "url": "https://feeds.megaphone.fm/adexchanger",
        "category": "programmatic"
    },
    {
        "name": "Marketecture",
        "url": "https://feeds.megaphone.fm/EAATE3740759293",
        "category": "adtech"
    },
    {
        "name": "The MadTech Podcast",
        "url": "https://audioboom.com/channels/4976875.rss",
        "category": "adtech"
    },
    {
        "name": "Paleo Ad Tech",
        "url": "https://paleoadtech.com/category/podcast/feed/",
        "category": "adtech"
    },
    {
        "name": "AdTechGod Pod",
        "url": "https://feeds.buzzsprout.com/2057436.rss",
        "category": "adtech"
    },

    # =====================
    # TIER 2 — Niche & Valuable (3 sources)
    # =====================
    {
        "name": "The CTV Podcast",
        "url": "https://feeds.acast.com/public/shows/the-ctv-podcast",
        "category": "ctv"
    },
    {
        "name": "Retail Media Breakfast Club",
        "url": "https://feeds.transistor.fm/retail-media-breakfast-club",
        "category": "retail_media"
    },
    {
        "name": "The Garage (Albertsons)",
        "url": "https://feeds.acast.com/public/shows/624489e813888000165b50f5",
        "category": "retail_media"
    },
]


# =============================================================
# SOCIAL / COMMUNITY FEEDS
# =============================================================
# These pull from social platforms via RSS.
# content_type field helps the UI distinguish social posts from articles.

# --- REDDIT ---
# Native RSS: add .rss to any subreddit URL
# Using /top/?t=week to get highest-signal posts, not noise
REDDIT_FEEDS = [
    {
        "name": "r/adops",
        "url": "https://www.reddit.com/r/adops/top/.rss?t=week",
        "category": "adtech",
        "content_type": "reddit"
    },
    {
        "name": "r/adtech",
        "url": "https://www.reddit.com/r/adtech/top/.rss?t=week",
        "category": "adtech",
        "content_type": "reddit"
    },
    {
        "name": "r/programmatic",
        "url": "https://www.reddit.com/r/programmatic/top/.rss?t=week",
        "category": "programmatic",
        "content_type": "reddit"
    },
    {
        "name": "r/digital_marketing",
        "url": "https://www.reddit.com/r/digital_marketing/top/.rss?t=week",
        "category": "advertising",
        "content_type": "reddit"
    },
    {
        "name": "r/PPC",
        "url": "https://www.reddit.com/r/PPC/top/.rss?t=week",
        "category": "programmatic",
        "content_type": "reddit"
    },
]

# --- BLUESKY ---
# Method: prepend openrss.org/ to any bsky.app profile URL
# These are verified Bluesky handles found via search
BLUESKY_FEEDS = [
    # --- Publications ---
    {
        "name": "AdExchanger (Bluesky)",
        "url": "https://openrss.org/bsky.app/profile/adexchanger.com",
        "category": "programmatic",
        "content_type": "bluesky"
    },
    {
        "name": "AdWeek (Bluesky)",
        "url": "https://openrss.org/bsky.app/profile/adweek.bsky.social",
        "category": "advertising",
        "content_type": "bluesky"
    },
    {
        "name": "PPC Land (Bluesky)",
        "url": "https://openrss.org/bsky.app/profile/ppc.land",
        "category": "programmatic",
        "content_type": "bluesky"
    },

    # --- Key Voices ---
    {
        "name": "Ari Paparo (Bluesky)",
        "url": "https://openrss.org/bsky.app/profile/aripaparo.com",
        "category": "adtech",
        "content_type": "bluesky"
    },
    {
        "name": "AdTechGod (Bluesky)",
        "url": "https://openrss.org/bsky.app/profile/adtechgod.com",
        "category": "adtech",
        "content_type": "bluesky"
    },

    # --- Digiday Reporters ---
    {
        "name": "Kimeko McCoy — Digiday (Bluesky)",
        "url": "https://openrss.org/bsky.app/profile/kimekom.bsky.social",
        "category": "media",
        "content_type": "bluesky"
    },
    {
        "name": "Krystal Scanlon — Digiday (Bluesky)",
        "url": "https://openrss.org/bsky.app/profile/krystalscanlon.bsky.social",
        "category": "media",
        "content_type": "bluesky"
    },
]

# --- MASTODON ---
# Method: append .rss to any Mastodon profile URL
# Ad tech / privacy / open-web crowd lives here
MASTODON_FEEDS = [
    # Add Mastodon profiles as you discover them:
    # {
    #     "name": "Person Name (Mastodon)",
    #     "url": "https://mastodon.social/@username.rss",
    #     "category": "privacy",
    #     "content_type": "mastodon"
    # },
]

# --- HACKER NEWS ---
# Filtered by keyword — only ad tech relevant posts
HACKERNEWS_FEEDS = [
    {
        "name": "Hacker News — Ad Tech",
        "url": "https://hnrss.org/newest?q=adtech+OR+advertising+OR+programmatic",
        "category": "adtech",
        "content_type": "hackernews"
    },
]

# --- SUBSTACK NEWSLETTERS ---
# Format: substackname.substack.com/feed
SUBSTACK_FEEDS = [
    {
        "name": "Marketecture Newsletter",
        "url": "https://marketecture.substack.com/feed",
        "category": "adtech",
        "content_type": "substack"
    },
    # Add more Substacks as you find them:
    # {
    #     "name": "Newsletter Name",
    #     "url": "https://name.substack.com/feed",
    #     "category": "adtech",
    #     "content_type": "substack"
    # },
]


# =============================================================
# MASTER FEED LIST — Combine all sources for the feed parser
# =============================================================
# The feed parser iterates over this single list.
# content_type defaults to "news" or "podcast" for legacy feeds.
ALL_FEEDS = (
    [dict(f, content_type="news") for f in NEWS_FEEDS]
    + [dict(f, content_type="podcast") for f in PODCAST_FEEDS]
    + REDDIT_FEEDS
    + BLUESKY_FEEDS
    + MASTODON_FEEDS
    + HACKERNEWS_FEEDS
    + SUBSTACK_FEEDS
)


# =============================================================
# CATEGORIES — Topic tags for auto-classification
# =============================================================
CATEGORIES = {
    "programmatic": {
        "display_name": "Programmatic",
        "keywords": ["programmatic", "dsp", "ssp", "rtb", "real-time bidding", "auction",
                     "bid", "impression", "exchange", "demand-side", "supply-side",
                     "header bidding", "prebid", "open auction", "private marketplace",
                     "curation", "supply path", "spo", "bid stream"]
    },
    "measurement": {
        "display_name": "Measurement",
        "keywords": ["measurement", "attribution", "brand lift", "viewability", "roi",
                     "analytics", "kpi", "conversion", "incrementality", "survey",
                     "attention", "outcomes", "mmm", "media mix", "brand study",
                     "brand safety", "brand suitability", "verification", "ias", "doubleverify"]
    },
    "privacy": {
        "display_name": "Privacy & Data",
        "keywords": ["privacy", "gdpr", "ccpa", "cookie", "cookieless", "consent",
                     "first-party", "third-party", "identity", "tracking",
                     "clean room", "data collaboration", "uid2", "unified id",
                     "contextual", "topics api", "privacy sandbox", "att"]
    },
    "ctv": {
        "display_name": "CTV & Video",
        "keywords": ["ctv", "connected tv", "ott", "streaming", "video", "television",
                     "linear", "cord-cutting", "avod", "fast", "roku", "netflix",
                     "disney+", "hulu", "peacock", "tubi", "freevee", "pluto",
                     "youtube tv", "amazon prime video", "apple tv+", "max"]
    },
    "retail_media": {
        "display_name": "Retail Media",
        "keywords": ["retail media", "rmn", "retail media network", "shopper",
                     "commerce media", "amazon ads", "walmart connect", "roundel",
                     "instacart", "kroger", "albertsons", "target", "best buy ads",
                     "offsite retail", "onsite retail", "sponsored products",
                     "citrus ad", "criteo retail", "meijer", "gopuff"]
    },
    "media": {
        "display_name": "Media & Publishing",
        "keywords": ["publisher", "media", "content", "editorial", "subscription",
                     "paywall", "audience", "reach", "engagement",
                     "news", "journalism", "digital media"]
    },
    "advertising": {
        "display_name": "Advertising & Creative",
        "keywords": ["creative", "campaign", "brand", "agency", "ad spend", "budget",
                     "advertiser", "marketing", "strategy",
                     "cmo", "holding company", "omnicom", "publicis", "wpp", "ipg",
                     "dentsu", "havas", "stagwell"]
    },
    "adtech": {
        "display_name": "Ad Tech",
        "keywords": ["ad tech", "adtech", "platform", "technology", "api", "integration",
                     "saas", "automation", "ai", "machine learning",
                     "martech", "madtech", "ad server", "ad ops",
                     "google antitrust", "trade desk", "dv360", "meta ads"]
    },
}


# =============================================================
# STOP WORDS — Ignore when analyzing trending topics
# =============================================================
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
