# FoodBridge

Web platform that connects surplus food donors, NGOs and volunteers.
AI features: (1) donation assistant reads a plain sentence (Claude API on the server, rule-based fallback in the browser), (2) smart NGO matching (weighted score).

## Run locally
    pip install -r requirements.txt
    set ANTHROPIC_API_KEY=your_key      (Windows)   |   export ANTHROPIC_API_KEY=your_key   (Mac/Linux)
    python app.py                       # open http://127.0.0.1:5000
Without a key the site still works with the rule-based assistant.

## Deploy (live link)
**Render (with Claude):** push this folder to GitHub, then Render > New > Web Service. Build: `pip install -r requirements.txt`. Start: `gunicorn app:app`. Add env var ANTHROPIC_API_KEY. The key lives only on the server, never in the HTML.
**GitHub Pages or Netlify (rule-based only):** upload `static/index.html` by itself.

## Tests
    pip install pytest && python -m pytest tests/test_app.py
    npm i jsdom && NODE_PATH=node_modules node tests/test_site.js static/index.html

## Known limits
Data is saved per browser (no shared database), no passwords, sample areas and distances.
Next phase: SQLite + login, real map distances, SMS notifications.
