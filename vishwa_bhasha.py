import uvicorn
import webbrowser
from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse

app = FastAPI(title="Vishwa Bhasha - Global Language Translation Core")

# 🧠 वैश्विक भाषाओं का डिक्शनरी मैप (विदेशी शब्दों को मलिकलैंग सिंटैक्स में बदलने के लिए)
LANGUAGE_DICTIONARY = {
    "spanish": {
        "crear": "banao",      # Variable definition
        "imprimir": "bolo",    # Print output
        "si": "agar",          # If condition
        "sino": "magar",        # Else condition
        "mientras": "jab_tak"   # Loop
    },
    "french": {
        "creer": "banao",
        "afficher": "bolo",
        "si": "agar",
        "sinon": "magar",
        "tant_que": "jab_tak"
    },
    "japanese": {
        "sakusei": "banao",
        "hyoji": "bolo",
        "moshimo": "agar",
        "soretomo": "magar",
        "aida": "jab_tak"
    }
}

def translate_to_maliklang(source_code: str, language: str) -> str:
    lang = language.lower()
    if lang not in LANGUAGE_DICTIONARY:
        return source_code
       
    words_map = LANGUAGE_DICTIONARY[lang]
    translated_lines = []
   
    # कोड की एक-एक लाइन को ट्रांसलेट करना
    for line in source_code.split('\n'):
        translated_line = line
        for foreign_word, maliklang_word in words_map.items():
            # शब्दों को मलिकलैंग सिंटैक्स से बदलना
            translated_line = translated_line.replace(foreign_word, maliklang_word)
        translated_lines.append(translated_line)
       
    return "\n".join(translated_lines)

# 🖥️ विश्व भाषा अनुवादक का इन-बिल्ट वेब इंटरफ़ेस
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="hi">
<head>
    <meta charset="UTF-8">
    <title>Vishwa Bhasha Translator</title>
    <style>
        body { font-family: 'Segoe UI', sans-serif; background: #0f172a; color: #f8fafc; padding: 40px; margin: 0; text-align: center; }
        .box { max-width: 800px; margin: 0 auto; background: #1e293b; padding: 30px; border-radius: 16px; border: 2px solid #3b82f6; box-shadow: 0 4px 20px rgba(59,130,246,0.25); }
        h1 { color: #3b82f6; margin-top: 0; }
        .tagline { color: #10b981; font-weight: bold; margin-bottom: 25px; }
        select, textarea { width: 95%; padding: 12px; background: #0f172a; color: white; border: 1px solid #475569; border-radius: 8px; font-size: 16px; margin-bottom: 15px; }
        textarea { height: 120px; font-family: monospace; resize: none; }
        button { width: 100%; padding: 12px; background: #3b82f6; color: white; border: none; border-radius: 8px; font-weight: bold; cursor: pointer; font-size: 16px; }
        button:hover { background: #2563eb; }
        .result-box { margin-top: 20px; padding: 15px; background: #0f172a; border-radius: 8px; border: 1px dashed #10b981; text-align: left; font-family: monospace; color: #38bdf8; white-space: pre-wrap; }
    </style>
</head>
<body>
    <div class="box">
        <h1>🌍 Vishwa Bhasha Translation System</h1>
        <div class="tagline"> लोगों को खुद खोजने दो, खुद का मालिक बनने दो! कोडिंग से अंग्रेजी का बंधन खत्म।</div>
       
        <label><b>अपनी वैश्विक भाषा चुनें (Select Global Language):</b></label><br>
        <select id="langSelect">
            <option value="spanish">Spanish (स्पैनिश)</option>
            <option value="french">French (फ्रेंच)</option>
            <option value="japanese">Japanese (जापानी)</option>
        </select>
       
        <label><b>अपनी भाषा में कोड लिखें (Write Code in Your Language):</b></label><br>
        <textarea id="sourceCode" placeholder="जैसे स्पैनिश में लिखें: \ncrear marks = 85\nsi marks >= 35\n    imprimir 'Pass!'"></textarea>
       
        <button onclick="convertCode()">🔄 मलिकलैंग कोड में बदलें (Translate Code)</button>
       
        <h3>💻 मलिकलैंग आउटपुट (Translated Maliklang AST Ready):</h3>
        <div id="outputArea" class="result-box">यहाँ आपका अनुवादित मलिकलैंग कोड दिखाई देगा...</div>
    </div>

    <script>
        async function convertCode() {
            let code = document.getElementById('sourceCode').value;
            let lang = document.getElementById('langSelect').value;
            if(!code) return alert('कृपया पहले कोई कोड दर्ज करें!');
           
            let output = document.getElementById('outputArea');
            output.innerText = "🤖 अनुवाद प्रक्रिया जारी है...";
           
            try {
                let response = await fetch(`/translate?code=${encodeURIComponent(code)}&lang=${lang}`);
                let text = await response.text();
                output.innerText = text;
            } catch(err) {
                output.innerText = "❌ अनुवाद विफल हुआ।";
            }
        }
    </script>
</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
async def home():
    return HTMLResponse(HTML_TEMPLATE)

@app.get("/translate")
async def translate(code: str = Query(...), lang: str = Query(...)):
    translated_code = translate_to_maliklang(code, lang)
    return translated_code

if __name__ == "__main__":
    print("🌍 विश्व भाषा अनुवाद कोर बैकग्राउंड में सक्रिय हो गया है...")
    webbrowser.open("http://127.0.0.1:8000")
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="error")
 
