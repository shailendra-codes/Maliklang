import uvicorn
import webbrowser
import sqlite3
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from typing import List
from cryptography.fernet import Fernet

app = FastAPI(title="Maliklang Super Connect Platform")

# 🔒 मिलिट्री-ग्रेड सुरक्षा की
SECRET_KEY = Fernet.generate_key()
cipher_suite = Fernet(SECRET_KEY)

# 💾 इन-बिल्ट डेटाबेस (SQLite) सेटअप - चैट हिस्ट्री के लिए
def init_db():
    conn = sqlite3.connect("super_history.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS secure_chats (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT
        )
    """)
    conn.commit()
    conn.close()

init_db()

class SecureManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)
       
        # 📂 पुराना डेटा सुरक्षित लोड करना
        conn = sqlite3.connect("super_history.db")
        cursor = conn.cursor()
        cursor.execute("SELECT content FROM secure_chats ORDER BY id ASC")
        rows = cursor.fetchall()
        conn.close()
       
        for row in rows:
          try:
                decrypted_text = cipher_suite.decrypt(row[0].encode()).decode()
                await websocket.send_text(decrypted_text)
            except:
                pass

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def broadcast(self, sender: str, text: str):
        # 🧠 एआई सुरक्षा फिल्टर
        if "fraud" in text.lower() or "hack" in text.lower():
            text = "⚠️ [सुरक्षा एआई द्वारा संदेश ब्लॉक किया गया]"

        formatted = f"💬 **{sender}**: {text}"
        encrypted = cipher_suite.encrypt(formatted.encode()).decode()

        # 💾 इतिहास सहेजना
        conn = sqlite3.connect("super_history.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO secure_chats (content) VALUES (?)", (encrypted,))
        conn.commit()
        conn.close()

        for connection in self.active_connections:
            await connection.send_text(formatted)

manager = SecureManager()

# 🖥️ बिना ऐप का इन-बिल्ट वेब पेज इंटरफेस
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Super Connect Dashboard</title>
    <style>
        body { font-family: sans-serif; background: #eef2f3; padding: 20px; }
        .box { max-width: 500px; margin: 0 auto; background: white; padding: 20px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
        #log { height: 200px; border: 1px solid #ddd; overflow-y: auto; background: #f9f9f9; padding: 10px; margin-bottom: 10px; border-radius: 5px; }
        input { width: 70%; padding: 8px; border: 1px solid #ddd; border-radius: 5px; }
        button { padding: 8px 15px; background: #2c3e50; color: white; border: none; border-radius: 5px; cursor: pointer; }
    </style>
</head>
<body>
    <div class="box">
        <h2>🛡️ Super Connect Dashboard</h2>
        <p>🔒 एआई सुरक्षा और चैट इतिहास सक्रिय है</p>
        <input type="text" id="myId" placeholder="अपनी पहचान ID डालें" style="width:93%; margin-bottom:10px;"><br>
        <button onclick="start()" style="width:100%; background:#27ae60; margin-bottom:10px;">सुरक्षित जुड़ें</button>
        <div id="log"></div>
        <input type="text" id="msg" placeholder="संदेश लिखें...">
        <button onclick="send()">भेजें</button>
    </div>
    <script>
        let ws;
        function start() {
            let id = document.getElementById('myId').value;
            if(!id) return alert('ID ज़रूरी है');
            ws = new WebSocket(`ws://127.0.0.1:8000/ws/${id}`);
            ws.onmessage = function(e) {
                let log = document.getElementById('log');
                log.innerHTML += '<div>' + e.data + '</div>';
                log.scrollTop = log.scrollHeight;
            };
            alert('सुपर सुरक्षित कनेक्शन तैयार है!');
        }
        function send() {
            let msg = document.getElementById('msg');
            ws.send(msg.value);
            msg.value = '';
        }
    </script>
</body>
</html>
"""

@app.get("/")
async def get():
    return HTMLResponse(HTML_TEMPLATE)

@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: str):
    await manager.connect(websocket)
    try:
        await manager.broadcast("सिस्टम एआई", f"🟢 [ID: {client_id}] सुरक्षित नेटवर्क में आ गए हैं।")
        while True:
            data = await websocket.receive_text()
            await manager.broadcast(client_id, data)
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast("सिस्टम एआई", f"🔴 [ID: {client_id}] नेटवर्क से बाहर चले गए।")

if __name__ == "__main__":
    webbrowser.open("http://127.0.0.1:8000")
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="error")
 
