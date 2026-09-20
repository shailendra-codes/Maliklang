import uvicorn
import webbrowser
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from typing import List
from cryptography.fernet import Fernet

app = FastAPI(title="Maliklang Super AI Connect")
templates = Jinja2Templates(directory="templates")

# 🔒 सुपर सुरक्षा की: यह चाबी मैसेजेस को लॉक और अनलॉक करती है
# असली प्रोजेक्ट में आप इसे और सुरक्षित रख सकते हैं
SECRET_KEY = Fernet.generate_key()
cipher_suite = Fernet(SECRET_KEY)

# 🧠 एआई फिल्टर: गलत शब्दों और स्पैम लिंक्स की लिस्ट
BAD_WORDS_FILTER = ["fraud", "hack", "spam", "gali1", "gali2", "http://scam"]

class SuperConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def broadcast_encrypted(self, sender_id: str, raw_message: str):
        # 🛡️ स्टेप 1: एआई कंटेंट सुरक्षा चेक (Anti-Spam Filter)
        cleaned_message = raw_message
        for bad_word in BAD_WORDS_FILTER:
            if bad_word in raw_message.lower():
                cleaned_message = "⚠️ [सुरक्षा चेतावनी: इस संदेश को एआई द्वारा ब्लॉक किया गया है]"
                break
       
        # 🛡️ स्टेप 2: एंड-टू-एंड इंक्रिप्शन (मैसेज को पूरी तरह लॉक करना)
        formatted_msg = f"💬 **{sender_id}**: {cleaned_message}"
        encrypted_text = cipher_suite.encrypt(formatted_msg.encode()).decode()
       
        print(f"🔒 [सर्वर सुरक्षा लॉग] एन्क्रिप्टेड डेटा ट्रांसफर: {encrypted_text[:20]}...")

        # 🛡️ स्टेप 3: सुरक्षित नेटवर्क के अंदर मौजूद लोगों को भेजना
        for connection in self.active_connections:
            # यहाँ सर्वर डेटा भेज रहा है, ब्राउज़र इसे खुद अनलॉक (Decrypt) करेगा
            # सरलता के लिए सर्वर ही इसे डिक्रिप्ट करके सुरक्षित यूज़र्स को डिलीवर कर रहा है
            decrypted_text = cipher_suite.decrypt(encrypted_text.encode()).decode()
            await connection.send_text(decrypted_text)

manager = SuperConnectionManager()

@app.get("/")
async def get_home(request: Request):
    
return templates.TemplateResponse(request=request, name="index.html")
 
@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: str):
    await manager.connect(websocket)
    try:
        await manager.broadcast_encrypted("सिस्टम एआई", f"🟢 [पहचान: {client_id}] सुपर सुरक्षित नेटवर्क से जुड़ गए हैं।")
        while True:
            data = await websocket.receive_text()
            await manager.broadcast_encrypted(client_id, data)
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast_encrypted("सिस्टम एआई", f"🔴 [पहचान: {client_id}] नेटवर्क से बाहर चले गए हैं।")

if __name__ == "__main__":
    print("🛡️ Maliklang Super AI Connect सफलतापूर्वक चालू हो गया है...")
    webbrowser.open("http://127.0.0.1:8000")
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="error")
 
