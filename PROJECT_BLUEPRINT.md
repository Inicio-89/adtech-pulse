# AdTech Pulse — Project Blueprint
## Complete Context, Goals, Architecture & Build Plan

---

## WHO IS BUILDING THIS

**Name:** Tim
**Day Job:** Account Development Representative (ADR) at Cint, transitioning to AE/AM role
**Team:** Media Measurement Team — focuses on brand lift studies and survey-based measurement
**Clients:** Forbes, LinkedIn, Disney, various media companies
**Coding Experience:** Has worked with Google Apps Script and Python via AI assistance (vibe coding), but hasn't written scripts from scratch. Comfortable with the concept of building things iteratively with AI help.
**Hardware:** Laptop with limited memory — need lightweight solutions
**Time Available:** 5-10 hours per week

---

## WHAT WE'RE BUILDING

**Project Name:** AdTech Pulse (working title — can change)

**One-line description:** A Python-powered, auto-curating website that aggregates advertising industry news and podcast content, analyzes trends and sentiment, and generates passive income through ads and affiliate links.

**The core idea:** Use Python to automatically pull content from public RSS feeds (ad industry news sites and podcasts), process and organize it, analyze trends and sentiment, and present it on a clean HTML/CSS website. Pair this with a newsletter digest, a trends dashboard, and original content/tools — all monetized through Google AdSense and affiliate marketing.

---

## WHY THIS PROJECT

### The Problem It Solves
Ad industry professionals need to stay current across dozens of sources — AdExchanger, AdWeek, Ad Age, Digiday, plus multiple podcasts. No single free resource aggregates all of this, analyzes what's trending, and adds sentiment context. The existing options are either paywalled trade publications or corporate blogs.

### Tim's Unfair Advantage
- Lives in the ad/measurement world daily — knows what matters and what doesn't
- Understands brand lift, media measurement, and campaign workflows from the inside
- Sales background gives natural storytelling and positioning skills
- Network of ad industry professionals on LinkedIn for distribution

### Revenue Model (No Selling Required)
- **Google AdSense:** Display ads on the site (requires ~some traffic to get approved)
- **Affiliate links:** Link to ad tech tools mentioned in articles (SEMrush, SimilarWeb, HubSpot, etc. pay $50-200+ per referral)
- **Newsletter sponsorships:** Once subscriber base grows, ad tech companies pay for newsletter placement
- **Zero upfront cost:** All tools and hosting are free tier

---

## THE FOUR LAYERS

Everything is ONE product with four layers that share the same Python backend and data:

### Layer 1: Auto-Curating Blog/Site (Foundation)
- Python pulls RSS feeds from 10-15 ad industry news sources and podcasts
- Content is stored in SQLite database
- Flask serves organized, categorized pages
- HTML/CSS frontend you fully control (for ad placement)
- Auto-updates multiple times daily with zero manual effort

### Layer 2: Newsletter Digest (Growth Engine)
- Weekly email digest of the top/most-discussed content from the site
- Built from the same data Layer 1 already collects
- Free via Mailchimp (up to 500 subscribers) or Buttondown
- Drives repeat traffic back to the site
- Builds an owned audience (email list = asset)

### Layer 3: Trends Dashboard (Differentiator)
- Visual page showing: what topics are hot this week, sentiment shifts, volume spikes
- Python analyzes word frequency across all aggregated content
- TextBlob or VADER (free Python libraries) for sentiment analysis
- No API costs — pure Python processing
- This is what makes the site MORE than just another aggregator

### Layer 4: Content Hub (Monetization Depth)
- Original articles and analysis written by Tim
- Tool features embedded in the site (built with Python)
- Affiliate links woven into relevant content naturally
- SEO-optimized content targeting ad industry search terms
- "Build in public" content documenting the journey

---

## TECH STACK (All Free or Near-Free)

### Backend (Python)
- **Flask** — lightweight Python web framework, serves HTML pages
- **feedparser** — parses RSS/podcast feeds (the core engine)
- **SQLite** — database that comes with Python, stores articles locally
- **TextBlob or VADER** — free sentiment analysis (no API needed)
- **collections.Counter** — Python built-in for trending topic detection
- **schedule or APScheduler** — automates feed pulling on a timer
- **Jinja2** — HTML templating (comes with Flask)

### Frontend
- **HTML** — page structure
- **CSS** — styling and layout
- **Minimal JavaScript** — only for interactive elements (charts, filters)

### Hosting & Deployment (Free Tier)
- **PythonAnywhere** or **Render** — free Python hosting with always-on capability
- **Custom domain** — ~$12/year (only cost)

### Content Sources (All Public RSS — No API Costs)
**News Feeds:**
- AdExchanger: https://feeds2.feedburner.com/ad-exchange-news
- AdWeek: https://adweek.com/feed
- Ad Age: https://adage.com (RSS available)
- Digiday: https://digiday.com/feed
- AdTech Daily: https://adtechdaily.com/feed
- PubMatic Blog: https://pubmatic.com/blog (RSS available)
- AdMonsters: https://admonsters.com (RSS available)
- VideoWeek: https://videoweek.com/feed

**Podcast Feeds:**
- AdExchanger Talks
- AdTech Unfiltered (by Basis/Noor Naseer)
- AdTechGod Pod
- Digiday Podcast
- Marketing Over Coffee
- ExchangeWire Podcast
- Slice of Ad Tech (Blockthrough)

---

## MONETIZATION PLAN

### Phase 1 (Months 1-3): Build & Launch
- No revenue expected — focus on building and getting content flowing
- Apply to Amazon Associates (easy approval)

### Phase 2 (Months 3-6): First Revenue
- Apply to Google AdSense once traffic starts
- Join affiliate programs: ShareASale, Impact.com (houses SEMrush, HubSpot, etc.)
- Start newsletter to build subscriber base

### Phase 3 (Months 6-12): Growth
- Ezoic or Mediavine for better ad rates (need ~10k monthly pageviews)
- Newsletter sponsorships ($50-200 per issue once list hits 1,000+)
- Affiliate revenue compounds as content library grows

### Target Affiliate Programs (Ad Tech Relevant)
- SEMrush (up to $200/referral)
- SimilarWeb
- HubSpot
- Google Workspace
- Ahrefs
- Mailchimp
- Various DSP/analytics platforms

---

## BUILD PHASES — DETAILED BREAKDOWN

### PHASE 1: MVP Site with News Aggregation (Weeks 1-3)
**Goal:** A working website that auto-pulls and displays ad industry news

**What you'll build:**
1. Flask application structure (app.py, templates/, static/)
2. RSS feed parser that pulls from 5 news sources
3. SQLite database to store articles
4. HTML/CSS homepage displaying latest articles
5. Category pages (Programmatic, Measurement, Privacy, CTV, etc.)
6. Basic navigation and clean layout

**What you'll learn:**
- How Flask routes work (URL → Python function → HTML page)
- How RSS feeds work and how feedparser processes them
- Basic SQL (storing and retrieving articles)
- HTML structure and CSS styling
- Jinja2 templating (Python variables in HTML)

**Files you'll create:**
```
adtech-pulse/
├── app.py                  # Main Flask application
├── feed_parser.py          # RSS feed pulling and processing
├── database.py             # SQLite setup and queries
├── config.py               # Feed URLs and settings
├── templates/
│   ├── base.html           # Shared layout (nav, footer, ad slots)
│   ├── index.html          # Homepage
│   ├── category.html       # Category page
│   └── article.html        # Single article view
├── static/
│   ├── css/
│   │   └── style.css       # All styling
│   └── js/
│       └── main.js         # Minimal interactivity
└── requirements.txt        # Python dependencies
```

**Key Python concepts used:**
- `feedparser.parse(url)` — fetches and parses RSS
- `sqlite3.connect()` — creates/connects to database
- `@app.route('/')` — maps URL to function
- `render_template()` — serves HTML with data
- `for entry in feed.entries` — loops through articles

---

### PHASE 2: Podcast Aggregation + Search (Weeks 4-6)
**Goal:** Add podcast episode feeds and a search function

**What you'll add:**
1. Podcast RSS feed parser (same feedparser library, podcast feeds)
2. Podcast listing page with episode descriptions, dates, audio links
3. Search functionality across all content
4. Topic tagging system (auto-categorize by keywords)
5. "Latest" and "Popular" sorting options

**What you'll learn:**
- How podcast RSS feeds differ from news feeds (enclosures, duration)
- SQL queries with WHERE and LIKE for search
- How to auto-tag content based on keyword matching
- More advanced Jinja2 (conditionals, filters)

**New files:**
```
├── podcast_parser.py       # Podcast-specific feed handling
├── tagger.py               # Auto-categorization by keywords
├── templates/
│   ├── podcasts.html       # Podcast listing page
│   ├── search.html         # Search results page
```

---

### PHASE 3: Trends Dashboard + Sentiment (Weeks 7-9)
**Goal:** A visual dashboard showing what's trending and industry sentiment

**What you'll add:**
1. Trending topics engine (word frequency analysis over time)
2. Sentiment analysis on article titles/descriptions
3. Dashboard page with visual charts
4. "This week vs last week" comparison
5. Topic-specific sentiment tracking

**What you'll learn:**
- Text processing with Python (tokenization, stopwords)
- TextBlob/VADER for sentiment scoring
- collections.Counter for frequency analysis
- Chart.js or basic SVG for data visualization
- How to present data insights visually

**New files:**
```
├── trends.py               # Trending topic detection
├── sentiment.py            # Sentiment analysis engine
├── templates/
│   ├── dashboard.html      # Trends dashboard page
```

**Python concepts:**
- `TextBlob(text).sentiment.polarity` — returns -1 to 1 sentiment score
- `Counter(words).most_common(20)` — top 20 trending terms
- Comparing this week's word frequencies vs last week's baseline

---

### PHASE 4: Newsletter + Monetization (Weeks 10-12)
**Goal:** Email newsletter, ad integration, affiliate links, polish

**What you'll add:**
1. Email signup form on the site
2. Newsletter generation script (auto-generates weekly digest)
3. Google AdSense integration (ad slots in HTML)
4. Affiliate link placement in relevant content
5. About page, contact, social links
6. SEO optimization (meta tags, sitemap, robots.txt)
7. Original content section for Tim's articles

**What you'll learn:**
- Email list management (Mailchimp/Buttondown API)
- How AdSense works and how to place ad units
- SEO basics (meta descriptions, structured data)
- How affiliate tracking works

**New files:**
```
├── newsletter.py           # Weekly digest generator
├── templates/
│   ├── newsletter_template.html  # Email template
│   ├── about.html          # About page
│   ├── blog.html           # Original content section
```

---

### PHASE 5+: Advanced Features (Month 4+)
**Future possibilities (once foundation is solid):**
- Auto-posting summaries to LinkedIn/Twitter
- AI-powered article summarization (when revenue covers API costs)
- User accounts and saved preferences
- Podcast transcript search (when budget allows)
- Mobile app version
- Premium newsletter tier

---

## HOW TO USE THIS DOCUMENT

### Starting a New Chat
Copy this entire document and paste it at the beginning of a new conversation with Claude. Say something like:

"Here's my project blueprint. I'm building AdTech Pulse — please read this for full context. I'm currently on [Phase X] and need help with [specific thing]."

### Tracking Progress
Update this section as you complete items:

- [ ] Phase 1: Flask app structure
- [ ] Phase 1: RSS feed parser working
- [ ] Phase 1: SQLite database storing articles
- [ ] Phase 1: HTML/CSS homepage
- [ ] Phase 1: Category pages
- [ ] Phase 1: Deployed to hosting
- [ ] Phase 2: Podcast feeds added
- [ ] Phase 2: Search functionality
- [ ] Phase 2: Auto-tagging system
- [ ] Phase 3: Trending topics engine
- [ ] Phase 3: Sentiment analysis
- [ ] Phase 3: Dashboard page
- [ ] Phase 4: Newsletter system
- [ ] Phase 4: AdSense integration
- [ ] Phase 4: Affiliate links placed
- [ ] Phase 4: SEO optimization

---

## KEY DECISIONS MADE

1. **Python + Flask + HTML/CSS** — not Streamlit (need full HTML control for ads)
2. **RSS feeds as data source** — no API costs, publicly available content
3. **Ad/affiliate revenue model** — not selling products directly
4. **Content-first approach** — start with content/newsletter, add tools later
5. **Advertising industry niche** — leverages Tim's domain expertise
6. **SQLite database** — lightweight, no server needed, comes with Python
7. **Free hosting** — PythonAnywhere or Render free tier
8. **Vibe coding approach** — build with AI assistance, learn as you go

---

## LEARNING GOALS

Throughout this project, Tim will learn:
- **Python fundamentals:** variables, functions, loops, dictionaries, classes
- **Flask web framework:** routes, templates, request handling
- **HTML/CSS:** page structure, styling, responsive design
- **SQL basics:** CREATE, INSERT, SELECT, WHERE queries
- **RSS/XML parsing:** how feeds work, feedparser library
- **Text analysis:** word frequency, sentiment analysis
- **Web deployment:** hosting, domains, DNS
- **SEO basics:** meta tags, sitemaps, structured data
- **Monetization:** AdSense, affiliate marketing, newsletter revenue
- **Git/GitHub:** version control and project documentation

---

## COSTS BREAKDOWN

| Item | Cost | When |
|------|------|------|
| Domain name | ~$12/year | Week 1 |
| Hosting (PythonAnywhere/Render) | Free | Week 1 |
| Python + all libraries | Free | Week 1 |
| Mailchimp (email) | Free up to 500 subs | Phase 4 |
| Google AdSense | Free (they pay you) | Phase 4 |
| Affiliate programs | Free to join | Phase 4 |
| **Total startup cost** | **~$12** | |

---

*Last updated: February 16, 2026*
*Current phase: Pre-Phase 1 (Planning Complete)*
