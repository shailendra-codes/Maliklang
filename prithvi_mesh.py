 import uvicorn
import webbrowser
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from typing import List

app = FastAPI(title="Prithvi Mesh - Off-Grid Emergency Network Simulator")

class PrithviMeshCore:
    def __init__(self):
        # 🌐 आपदा नेटवर्क: बिना इंटरनेट और मोबाइल टावर के आपस में जुड़े डिवाइस
        self.active_devices: List[WebSocket] = []

    async def register_device(self, websocket: WebSocket):
        await websocket.accept()
        self.active_devices.append(websocket)

    def unregister_device(self, websocket: WebSocket):
        self.active_devices.remove(websocket)

    async def broadcast_sos_signal(self, sender_id: str, message: str, location: str):
        # 🚨 लाइफ-सेवर एक्शन: संकट के समय संदेश को बिना सर्वर के आगे भेजना
        formatted_sos = f"🚨 [SOS आपातकालीन अलर्ट] नोड: **{sender_id}** | स्थान: {location} | संदेश: {message}"
        for device in self.active_devices:
            await device.send_text(formatted_sos)

mesh_engine = PrithviMeshCore()

# 🖥️ बिना इंटरनेट के काम करने वाले स्क्रीनलेस सिमुलेटर का वेब इंटरफ़ेस
HTML_INTERFACE = """
<!DOCTYPE html>
<html lang="hi">
<head>
    <meta charset="UTF-8">
    <title>Prithvi Mesh Emergency Console</title>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: #1e1b4b; color: #f8fafc; text-align: center; padding: 30px; margin: 0; }
        .emergency-box { max-width: 650px; margin: 0 auto; background: #312e81; padding: 30px; border-radius: 16px; border: 2px solid #ef4444; box-shadow: 0 4px 25px rgba(239,68,68,0.3); }
        h1 { color: #ef4444; font-size: 32px; margin-top: 0; }
        .status { color: #10b981; font-weight: bold; font-size: 14px; margin-bottom: 25px; }
        #sos-log { height: 200px; border: 1px solid #4338ca; background: #1e1b4b; padding: 15px; overflow-y: auto; text-align: left; border-radius: 8px; margin-bottom: 20px; color: #fca5a5; font-family: monospace; }
        input { width: 92%; padding: 12px; border: 1px solid #4338ca; background: #1e1b4b; color: white; border-radius: 8px; font-size: 16px; margin-bottom: 15px; }
        button { width: 100%; padding: 12px; background: #ef4444; color: white; border: none; border-radius: 8px; font-weight: bold; cursor: pointer; font-size: 16px; }
        button:hover { background: #dc2626; }
    </style>
</head>
<body>
    <div class="emergency-box">
        <h1>🛰️ Prithvi Mesh Emergency Node</h1>
        <div class="status">🟢 सिम कार्ड मुक्त | मोबाइल टावर मुक्त | स्थानीय आपदा तरंगें सक्रिय</div>
       
        <input type="text" id="deviceId" placeholder="अपनी डिवाइस ID दर्ज करें..."><br>
        <button onclick="connectMesh()" style="background:#10b981; margin-bottom:20px;">आपदा नेटवर्क नोड चालू करें</button>
       
        <div id="sos-log">ℹ️ बाढ़, भूकंप या आपातकाल में बिना इंटरनेट संदेश भेजने के लिए तैयार...</div>
       
        <input type="text" id="locInput" placeholder="अपना वर्तमान स्थान (Location) लिखें..."><br>
        <input type="text" id="sosMsg" placeholder="मदद का संदेश (जैसे: भोजन और पानी की ज़रूरत है)..."><br>
        <button onclick="sendSOS()">🚨 आपातकालीन SOS सिग्नल भेजें</button>
    </div>

    <script>
        let ws;
        function connectMesh() {
            let id = document.getElementById('deviceId').value;
            if(!id) return alert('कृपया डिवाइस ID दर्ज करें!');
           
            ws = new WebSocket(`ws://127.0.0.1:8000/ws/${id}`);
           
            ws.onmessage = function(event) {
                let log = document.getElementById('sos-log');
                if(log.innerText.startsWith('ℹ️')) log.innerText = '';
                log.innerHTML += '<div>' + event.data + '</div>';
                log.scrollTop = log.scrollHeight;
            };
            alert('🛰️ पृथ्वी मेश एक्टिव! मोबाइल टावर गिरने पर भी संचार सुरक्षित है।');
        }

        function sendSOS() {
            let loc = document.getElementById('locInput').value;
            let msg = document.getElementById('sosMsg').value;
            if(!loc || !msg) return alert('स्थान और संदेश दोनों ज़रूरी हैं!');
           
            // डेटा को एक साझा फॉर्मेट में भेजना
            ws.send(JSON.stringify({ location: loc, message: msg }));
            document.getElementById('sosMsg').value = '';
        }
    </script>
</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
async def get_interface():
    return HTMLResponse(HTML_INTERFACE)

import json

@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: str):
    await mesh_engine.register_device(websocket)
    try:
        await mesh_engine.broadcast_sos_signal("सिस्टम अलर्ट", f"नोड {client_id} आपातकालीन ग्रिड से जुड़ गया है।", "लोकल")
      while True:
            data = await websocket.receive_text()
            # JSON डेटा को पढ़ना
            try:
                parsed_data = json.loads(data)
                await mesh_engine.broadcast_sos_signal(client_id, parsed_data['message'], parsed_data['location'])
            except:
                await mesh_engine.broadcast_sos_signal(client_id, data, "अज्ञात")
    except WebSocketDisconnect:
        mesh_engine.unregister_device(websocket)
        await mesh_engine.broadcast_sos_signal("सिस्टम अलर्ट", f"नोड {client_id} ग्रिड से बाहर हो गया है।", "लोकल")

if __name__ == "__main__":
    print("🛰️ पृथ्वी मेश आपातकालीन नेटवर्क सक्रिय हो रहा है...")
    webbrowser.open("http://127.0.0.1:8000")
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="error")
 
