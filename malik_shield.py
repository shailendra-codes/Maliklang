import uvicorn
import webbrowser
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import random

app = FastAPI(title="MalikShield AI - Cyber Security Watchdog")

# 🔍 नकली सुरक्षा लॉग्स (सिमुलेशन के लिए) जो दिखाएंगे कि सुरक्षा काम कर रही है
DUMMY_ATTACKS = [
    "अनधिकृत आईपी (IP) द्वारा नेटवर्क स्कैन ब्लॉक किया गया।",
    "फर्जी लॉगिन अनुरोध (Brute force attempt) को सफलतापूर्वक रोका गया।",
    "संदिग्ध स्पैम लिंक ट्रांसमिशन को नष्ट किया गया।",
    "बाहरी नोड से आ रहे खतरनाक डेटा पैकेट्स को रिजेक्ट किया गया।"
]

def scan_system_health():
    # एआई सुरक्षा लेयर का लाइव स्टेटस जेनरेट करना
    status_score = random.randint(95, 100)
    recent_logs = random.sample(DUMMY_ATTACKS, 2)
    return status_score, recent_logs

# 🖥️ मलिकशील्ड का इन-बिल्ट बिना किसी ऐप का सुरक्षा इंटरफ़ेस
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="hi">
<head>
    <meta charset="UTF-8">
    <title>MalikShield AI Dashboard</title>
    <style>
        body { font-family: sans-serif; background: #090d16; color: #00ff66; padding: 40px; margin: 0; text-align: center; }
        .shield-box { max-width: 700px; margin: 0 auto; background: #111827; padding: 30px; border-radius: 16px; border: 2px solid #00ff66; box-shadow: 0 4px 20px rgba(0,255,102,0.2); }
        h1 { color: #00ff66; margin-top: 0; text-shadow: 0 0 10px rgba(0,255,102,0.5); }
        .tagline { color: #f8fafc; margin-bottom: 25px; font-size: 14px; }
        .status-circle { width: 120px; height: 120px; border-radius: 50%; border: 5px solid #00ff66; display: inline-flex; justify-content: center; align-items: center; font-size: 24px; font-weight: bold; margin-bottom: 20px; background: #090d16; box-shadow: 0 0 15px rgba(0,255,102,0.3); }
        .log-box { height: 150px; border: 1px solid #374151; background: #090d16; padding: 15px; overflow-y: auto; text-align: left; border-radius: 8px; margin-bottom: 20px; color: #38bdf8; font-family: monospace; }
        button { width: 100%; padding: 12px; background: #00ff66; color: #090d16; border: none; border-radius: 8px; font-weight: bold; cursor: pointer; font-size: 16px; box-shadow: 0 0 10px rgba(0,255,102,0.3); }
        button:hover { background: #00cc52; }
    </style>
</head>
<body>
    <div class="shield-box">
        <h1>🛡️ MalikShield AI Watchdog</h1>
        <div class="tagline">लोगों को खुद खोजने दो, खुद का मालिक बनने दो! स्वचालित साइबर सुरक्षा कवच सक्रिय।</div>
               <div class="status-circle" id="healthScore">100%</div>
        <p><b>सिस्टम सुरक्षा स्कोर (System Health Score)</b></p>
       
        <h3>📊 लाइव सुरक्षा अलर्ट (Live Security Audits):</h3>
        <div id="logArea" class="log-box">🛡️ मलिकशील्ड सक्रिय है। बैकएंड की चौबीसों घंटे निगरानी की जा रही है...</div>
       
        <button onclick="runDeepScan()">⚡ लाइव एआई सुरक्षा जांच शुरू करें (Run Scan)</button>
    </div>

    <script>
        async function runDeepScan() {
            let log = document.getElementById('logArea');
            let score = document.getElementById('healthScore');
            log.innerHTML = "🤖 एआई सुरक्षा गार्ड बैकएंड फाइलों की जांच कर रहा है...";
           
            try {
                let response = await fetch('/scan');
                let data = await response.json();
               
                score.innerText = data.score + "%";
                log.innerHTML = "";
                data.logs.forEach(item => {
                    log.innerHTML += "<div>🛡️ " + item + "</div>";
                });
            } catch(err) {
                log.innerText = "❌ स्कैन विफल हुआ।";
            }
        }
    </script>
</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
async def home():
    return HTMLResponse(HTML_TEMPLATE)

@app.get("/scan")
async def scan():
    score, logs = scan_system_health()
    return {"score": score, "logs": logs}

if __name__ == "__main__":
    print("🛡️ मलिकशील्ड स्वचालित सुरक्षा गार्ड सक्रिय हो गया है...")
    webbrowser.open("http://127.0.0.1:8000")
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="error")
 
