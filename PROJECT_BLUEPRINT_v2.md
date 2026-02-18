# AdTech Pulse — Project Blueprint v2
## Updated February 18, 2026

---

## PROJECT STATUS

**Current state:** Phase 1 complete. Site runs locally with 5 news feeds + 2 podcast feeds pulling ~62 articles. GitHub repo live at github.com/Inicio-89/adtech-pulse.

**What just happened (Session 3):** Expanded config.py from 7 feeds to 46+ sources across news, podcasts, Reddit, Bluesky, Mastodon, Hacker News, and Substack. Designed distribution strategy. Explored brand names. Designed prospecting intelligence architecture (private, separate from public site).

**Next action when at PC:** Replace config.py, delete old database, run app.py, push to GitHub.

---

## WHO IS BUILDING THIS

- **Name:** Tim
- **Day job:** ADR at Cint → transitioning to AE/AM. Media Measurement Team.
- **Expertise:** Brand lift studies, survey-based measurement. Clients include Forbes, LinkedIn, Disney.
- **Coding:** Google Apps Script + Python via AI assistance (vibe coding). Hasn't written scripts from scratch.
- **Hardware:** Laptop with limited memory. 5-10 hours/week for side projects.
- **GitHub:** Inicio-89

---

## WHAT THIS IS

**One-liner:** A Python-powered ad tech news aggregator that pulls from 46+ public sources, organizes by topic, and serves as both a media brand and a private prospecting engine.

**The real play:** Two products sharing one database:
1. **PUBLIC SITE** — Legitimate ad tech aggregator anyone in the industry would read
2. **PRIVATE LAYER** — Prospecting intelligence tool only Tim sees (admin login or separate script)

The public site builds credibility and audience. The private layer surfaces outreach triggers from the same content. Nobody visiting the site ever sees the sales tooling.

---

## ARCHITECTURE: THE FIVE LAYERS

### Layer 1: Content Aggregation (Foundation) ✅ BUILT
- Python pulls RSS feeds from 46+ sources
- SQLite database stores articles
- Flask serves organized, categorized pages
- Auto-updates with zero manual effort

### Layer 2: Multi-Platform Distribution (Growth Engine)
- Substack weekly digest → owns email list
- Medium for longer analysis → SEO + discovery
- Reddit engagement → authentic community presence
- Bluesky/Mastodon → real-time takes
- LinkedIn last → show up with portfolio, not empty-handed

### Layer 3: Trends Dashboard (Differentiator)
- 7-day lookback window analyzing all content
- Word frequency / topic spike detection
- "Trending This Week" homepage section
- Auto-generated trend summaries for blog/newsletter

### Layer 4: Content Hub (Monetization Depth)
- Original analysis written by Tim
- Affiliate links woven into relevant content
- AdSense integration
- SEO-optimized pages targeting ad industry searches

### Layer 5: Prospecting Intelligence (Private — Never Public)
- Admin-only dashboard behind login OR separate Python script
- Tags articles by company name from prospect list
- Flags trigger events: new campaigns, hires, funding, RFPs
- Exports matches to Google Sheet for outreach tracking
- "Flag for outreach" button visible only when logged in as admin

---

## CONTENT SOURCES: THE FULL MAP (46+ feeds)

| Source Type | Count | What It Gives You |
|---|---|---|
| Trade press RSS (Tier 1) | 9 | Polished industry reporting |
| Vendor/platform blogs (Tier 2) | 10 | Company positioning, product launches |
| Niche/retail media (Tier 3) | 5 | Vertical intelligence |
| Podcasts (Tier 1 + 2) | 8 | Long-form expert conversation |
| Reddit subreddits | 5 | Unfiltered practitioner opinions |
| Bluesky profiles | 7 | Real-time industry reaction, hot takes |
| Mastodon profiles | TBD | Privacy/open-web technical crowd |
| Hacker News | 1 | Tech-forward perspective |
| Substack newsletters | 1+ | Deep-dive independent analysis |

---

## DISTRIBUTION STRATEGY

### Phase A — Plant Flags (This Week)
1. **Substack** — Weekly digest "This Week in Ad Tech." Owns email list.
2. **Medium** — Republish longer analysis. Built-in SEO.
3. **Reddit** — Join r/adops, r/adtech, r/programmatic. Lurk first, contribute authentically, never self-promote.
4. **Bluesky** — Claim handle, share short takes.

### Phase B — Build Social Layer (Weeks 2-4)
5. **Mastodon** — Privacy/open-web crowd.
6. **Threads** — Low effort if already posting elsewhere.

### Phase C — Go Where Money Is (Month 2+)
7. **LinkedIn** — Only after having 8-12 published pieces, active Reddit karma, 20+ source site.

### Content Tone
- NOT LinkedIn thought leadership (one-line openers, arrows, "what do you think?")
- Write like texting a coworker about an article you just read
- Mix of: short casual takes, article shares with 1-2 sentence opinion, longer original analysis on site shared as link
- Comment on others' posts more than creating own

### Attribution System
Every piece of content shows: source name, link to original, author name when possible. Analysis posts have "Sources" section at bottom. Standing "Sources & Attribution" page on site. Footer disclaimer already exists.

---

## BUILD PHASES — REVISED

### ✅ PHASE 1: MVP (COMPLETE)
- Flask app structure
- RSS feed parser (5 news + 2 podcast feeds)
- SQLite database with unique URL constraint
- HTML/CSS homepage, category pages, podcast page, search, about
- GitHub repo live

### PHASE 2: Scale & Stabilize (Current — Weeks 3-4)
**Goal:** Expand sources, add retention, improve reliability

**2A — Feed Expansion (next PC session):**
- [ ] Replace config.py with expanded version (24 news + 8 podcast + social feeds)
- [ ] Delete old database, rebuild with new sources
- [ ] Update feed_parser.py to handle content_type field (reddit, bluesky, etc.)
- [ ] Add user-agent header for Reddit RSS (Reddit blocks default Python UA)
- [ ] Test all feeds pulling correctly
- [ ] Push to GitHub

**2B — 7-Day Retention + Trending:**
- [ ] Modify database.py to keep articles minimum 7 days
- [ ] Schedule feed fetches multiple times per day
- [ ] Build trending engine: analyze last 7 days, find most-mentioned topics/companies/themes
- [ ] "Trending This Week" section on homepage
- [ ] Auto-generated trend summaries

**2C — Site Polish:**
- [ ] Privacy Policy page (required for AdSense)
- [ ] Terms of Use page
- [ ] Sources & Attribution page
- [ ] "Last updated" timestamp in footer
- [ ] Mobile-first CSS improvements
- [ ] Social content displayed differently from articles (labeled as "Community" or "Social")

### PHASE 3: Distribution + Content (Weeks 5-8)
**Goal:** Start publishing, build audience

- [ ] Claim platform names: Substack, Medium, Reddit account, Bluesky handle
- [ ] Write first Substack digest from trending data
- [ ] Publish first Medium article (original analysis using site data)
- [ ] Start engaging in Reddit threads (r/adops, r/adtech, r/programmatic)
- [ ] Set up Bluesky, start sharing links with short takes
- [ ] Deploy site to Render or PythonAnywhere (make it public)
- [ ] Custom domain (~$12/year)
- [ ] Apply for Amazon Associates (easy approval)

### PHASE 4: Monetization + Newsletter (Weeks 9-12)
**Goal:** Revenue layers, email list

- [ ] Email signup form on site (Substack embeds or Buttondown)
- [ ] Weekly newsletter auto-generation from trending data
- [ ] Apply for Google AdSense
- [ ] Join affiliate programs (ShareASale, Impact.com)
- [ ] Affiliate links in relevant content (SEMrush, SimilarWeb, HubSpot)
- [ ] SEO optimization (meta tags, sitemap, robots.txt)
- [ ] Original content section for Tim's analysis pieces
- [ ] LinkedIn presence (with 8-12 published pieces as portfolio)

### PHASE 5: Prospecting Intelligence (Month 4+)
**Goal:** Private outreach layer — never visible on public site

- [ ] Admin login system (simple Flask-Login)
- [ ] "Flag for outreach" button on article cards (visible only when admin logged in)
- [ ] Saved/flagged articles view (admin-only route)
- [ ] Keyword detection for company names from prospect list
- [ ] Trigger categorization (new campaign, hire, funding, RFP, product launch)
- [ ] Export to Google Sheet for outreach tracking
- [ ] OR: Separate Python script that reads same database, outputs to Sheet

### PHASE 6+: Advanced (Month 6+)
- Sentiment analysis (TextBlob/VADER on titles + descriptions)
- Dashboard with visual charts (Chart.js)
- Auto-posting summaries to social platforms
- AI-powered article summarization (when revenue covers API costs)
- Video content: 90-second weekly recaps from phone
- Premium newsletter tier

---

## BRAND NAME STATUS

**Current:** AdTech Pulse (working title)
**Decision pending between two directions:**
- **Parnoise** — parse + noise. Invented word, poetic, says what it does
- **Noisecut** — direct, aggressive, memorable

**Names explored and rejected:** Murmur (taken — media agency), Adlore (medical device company), Lumivore (French production company), Adthentic (German ad company), Noiseless (too crowded), Parsignal (domain squatted), ClearSignal (telecom company). Also considered: Parallax, Lumen, Meridian, Planck, Candela, Parsec, Beacon, Cipher, Prism, and many others.

**Important:** Finalize name BEFORE claiming platform handles on Substack, Medium, Reddit, Bluesky.

---

## TECH STACK

| Component | Tool | Cost |
|---|---|---|
| Backend | Python + Flask | Free |
| Feed parser | feedparser library | Free |
| Database | SQLite | Free |
| Frontend | HTML + CSS + minimal JS | Free |
| Hosting | Render or PythonAnywhere | Free tier |
| Domain | Custom | ~$12/year |
| Email list | Substack or Buttondown | Free |
| Newsletter | Auto-generated from trending data | Free |
| Ads | Google AdSense | Free (they pay you) |
| Affiliates | ShareASale, Impact.com | Free to join |
| Version control | GitHub (Inicio-89) | Free |

**Total startup cost: ~$12/year for domain**

---

## KEY DECISIONS MADE

1. Python + Flask + HTML/CSS (not Streamlit — need full HTML control for ads)
2. RSS feeds as data source (no API costs, publicly available)
3. Content INDEXES headlines/excerpts and links out — never republishes full articles
4. Prospecting intelligence layer is PRIVATE (admin-only or separate script)
5. Public site has zero hint of sales tooling
6. Distribution starts with Substack/Medium/Reddit, LinkedIn comes LAST
7. Content tone: casual colleague, not LinkedIn thought leader
8. Brand name undecided — finalize before claiming platform handles
9. Mobile-first development
10. Git/GitHub from day one (Inicio-89/adtech-pulse)

---

## KEY FILE PATHS

- **Project root:** `D:\adtech-hub`
- **GitHub repo:** `https://github.com/Inicio-89/adtech-pulse`
- **Database:** `D:\adtech-hub\adtech_pulse.db` (auto-created by app.py)

---

## HOW TO USE THIS DOCUMENT

Paste into any new Claude chat with:
> "Here's my project blueprint. I'm building AdTech Pulse — please read this for full context. I'm currently on [Phase X] and need help with [specific thing]."

---

*Last updated: February 18, 2026*
*Current phase: Phase 2A — Feed Expansion*
