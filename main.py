from flask import Flask, jsonify, render_template, request
from threats.malware import MalwareThreat
from threats.phishing import PhishingThreat
from threats.brute_force import BruteForceThreat
from threats.sql_injection import SQLInjectionThreat
from engine import ThreatEngine

app = Flask(__name__, template_folder='.', static_folder='.', static_url_path='')

scans_data = [
    {"type": "malware",  "target": "C:/Windows/update.exe",   "value": ".exe"},
    {"type": "malware",  "target": "C:/Downloads/report.pdf", "value": ".pdf"},
    {"type": "phishing", "target": "user@company.com",        "value": "http://secure-bank-login-verify.com"},
    {"type": "phishing", "target": "admin@company.com",       "value": "https://newsletter.company.com"},
    {"type": "brute",    "target": "admin@server",            "value": "14"},
    {"type": "brute",    "target": "user@server",             "value": "2"},
    {"type": "sql",      "target": "login_form",              "value": "' OR 1=1; DROP TABLE users--"},
    {"type": "sql",      "target": "search_bar",              "value": "laptop bags"},
]

def build_engine():
    engine = ThreatEngine()
    for s in scans_data:
        if s["type"] == "malware":
            engine.load(MalwareThreat(s["target"], s["value"]))
        elif s["type"] == "phishing":
            engine.load(PhishingThreat(s["target"], s["value"]))
        elif s["type"] == "brute":
            engine.load(BruteForceThreat(s["target"], int(s["value"])))
        elif s["type"] == "sql":
            engine.load(SQLInjectionThreat(s["target"], s["value"]))
    engine.run_all()
    return engine

@app.route('/')
@app.route('/CyberShield/')
def index():
    return render_template('index.html')

@app.route('/api/scans')
def get_scans():
    engine = build_engine()
    results = []
    for i, t in enumerate(engine.threats):
        results.append({
            "id": i + 1,
            "name": t.name,
            "severity": t.severity,
            "target": t.target,
            "detected": t.is_detected,
            "details": t.details,
            "type": scans_data[i]["type"]
        })
    return jsonify(results)

if __name__ == '__main__':
    app.run(port=5000, debug=True)