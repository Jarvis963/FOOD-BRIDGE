import json, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import app
c = app.app.test_client()
URL = "/api/analyze"
def test_empty(): assert c.post(URL, json={"text": ""}).status_code == 400
def test_no_key(monkeypatch):
    monkeypatch.delenv("ANTHROPIC_API_KEY", raising=False)
    assert c.post(URL, json={"text": "10 plates rice"}).status_code == 503
def test_ok_and_sanitised(monkeypatch):
    monkeypatch.setenv("ANTHROPIC_API_KEY", "x")
    out = {"item": "Veg biryani", "category": "Weapon", "servings": 40, "allergens": ["Dairy", "Lead"],
           "hours_since_prepared": 1, "safe_hours_total": 4, "verdict": "ok", "notes": []}
    monkeypatch.setattr(app, "ask_claude", lambda t: "```json\n" + json.dumps(out) + "\n```")
    r = c.post(URL, json={"text": "40 plates biryani"})
    assert r.status_code == 200 and r.json["category"] == "Other" and r.json["allergens"] == ["Dairy"]
def test_bad_output(monkeypatch):
    monkeypatch.setenv("ANTHROPIC_API_KEY", "x")
    monkeypatch.setattr(app, "ask_claude", lambda t: "not json")
    assert c.post(URL, json={"text": "rice"}).status_code == 502
