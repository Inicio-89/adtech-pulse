# AdTech Pulse — Setup & Run Guide

## What This Is
A Python-powered website that automatically aggregates advertising industry news and podcast content from public RSS feeds. Built with Flask (Python), HTML, and CSS.

## Quick Start (5 minutes)

### Step 1: Make sure Python is installed
Open your terminal/command prompt and type:
```
python --version
```
You need Python 3.8 or higher. If you don't have it, download from https://python.org

### Step 2: Install dependencies
Navigate to the project folder and run:
```
cd adtech-pulse
pip install -r requirements.txt
```
This installs Flask and feedparser.

### Step 3: Run the app
```
python app.py
```
This will:
1. Create the SQLite database (adtech_pulse.db)
2. Fetch content from all RSS feeds (takes 30-60 seconds first time)
3. Start the web server

### Step 4: Open in your browser
Go to: http://localhost:5000

That's it! You should see the site with real ad industry content.

## Project Structure
```
adtech-pulse/
├── app.py              # Main Flask app (routes & pages)
├── feed_parser.py      # RSS feed fetching engine
├── database.py         # SQLite database operations
├── config.py           # Feed URLs & settings (edit to add sources)
├── requirements.txt    # Python dependencies
├── templates/          # HTML templates (what users see)
│   ├── base.html       # Shared layout (nav, sidebar, footer)
│   ├── index.html      # Homepage
│   ├── category.html   # Topic pages
│   ├── podcasts.html   # Podcast listing
│   ├── search.html     # Search results
│   ├── about.html      # About page
│   └── refresh.html    # Feed refresh status
├── static/
│   ├── css/style.css   # All styling
│   └── js/main.js      # Minimal JavaScript
└── adtech_pulse.db     # Database (created automatically)
```

## Common Tasks

### Add a new RSS feed source
Edit `config.py` and add to NEWS_FEEDS or PODCAST_FEEDS:
```python
{
    "name": "Source Name",
    "url": "https://example.com/feed",
    "category": "programmatic"
}
```

### Manually refresh feeds
Visit http://localhost:5000/refresh in your browser

### Add a new topic category
Edit `config.py` and add to CATEGORIES with keywords for auto-tagging

### Change the site design
Edit `static/css/style.css` — all colors are in CSS variables at the top

## Next Phases
See PROJECT_BLUEPRINT.md for the full roadmap including:
- Phase 2: Search & podcast improvements
- Phase 3: Trends dashboard & sentiment analysis
- Phase 4: Newsletter, ads, affiliate links
