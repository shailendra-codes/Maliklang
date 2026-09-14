import uvicorn
import webbrowser
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from typing import List

app = FastAPI(title="Divya Drishti - Advanced Video & Audio Telepathy Simulator")

class DivyaDrishtiCore:
    def __init__(self):
        # 🌐 मेश नेटवर्क: बिना मोबाइल या सिम के जुड़े हुए एक्टिव नोड्स (यूज़र्स)
        self.active_connections: List[WebSocket] = []

    async def connect_node(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect_node(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def transmit_wave(self, sender_node: str, raw_data: str):
        # 🛡️ चेतना प्रसारण: वॉइस, टेक्स्ट और सिग्नल डेटा को मेश नेटवर्क में भेजना
        formatted_wave = f"👁️ [दिव्य दृष्टि] **{sender_node}**: {raw_data}"
        for connection in self.active_connections:
            await connection.send_text(formatted_wave)

telepathy_engine = DivyaDrishtiCore()

# 🖥️ बिना मोबाइल/स्क्रीन के सीधे ब्राउज़र आधारित वियरेबल गैजेट का सिमुलेशन पेज
HTML_INTERFACE = """
<!DOCTYPE html>
<html lang="hi">
<head>
    <meta charset="UTF-8">
    <title>Divya Drishti Live Console</title>
    <style>
        body { font-family: 'Georgia', serif; background: #0f172a; color: #e2e8f0; text-align: center; padding: 30px; margin: 0; }
        .console-box { max-width: 750px; margin: 0 auto; background: #1e293b; padding: 25px; border-radius: 16px; border: 2px solid #e67e22; box-shadow: 0 4px 25px rgba(230,126,34,0.3); }
        h1 { color: #e67e22; font-size: 32px; margin-bottom: 5px; margin-top: 0; }
        .status { color: #10b981; font-weight: bold; font-size: 14px; margin-bottom: 20px; }
       
        /* 👁️ लाइव दृश्य के लिए लेआउट */
        .vision-area { display: flex; gap: 15px; margin-bottom: 20px; justify-content: center; align-items: flex-start; }
        #myVideo { width: 45%; border-radius: 10px; border: 2px dashed #e67e22; background: #000; transform: scaleX(-1); }
        #wave-log { width: 45%; height: 165px; border: 1px solid #475569; background: #0f172a; padding: 10px; overflow-y: auto; text-align: left; border-radius: 8px; color: #38bdf8; font-family: monospace; font-size: 13px; }
       
        input { width: 75%; padding: 12px; border: 1px solid #475569; background: #1e293b; color: white; border-radius: 8px; font-size: 16px; }
        button { padding: 12px 20px; background: #e67e22; color: white; border: none; border-radius: 8px; font-weight: bold; cursor: pointer; font-size: 16px; }
        button:hover { background: #d35400; }
    </style>
</head>
<body>
    <div class="console-box">
        <h1>👁️ Sanjay Divya-Drishti Live Protocol</h1>
        <div class="status">🌐 मुफ़्त सैटेलाइट मेश नेटवर्क | लाइव दृश्य (Video) और श्रवण (Audio) सक्रिय</div>
       
        <input type="text" id="nodeId" placeholder="अपनी दिव्य पहचान (ID) दर्ज करें..." style="width:92%; margin-bottom:15px;"><br>
        <button onclick="activateDrishti()" style="width:100%; background:#27ae60; margin-bottom:20px; font-weight:bold;">दिव्य चेतना और लाइव कैमरा सक्रिय करें</button>
       <!-- 🎥 लाइव देखने और सुनने का संयुक्त एरिया -->
        <div class="vision-area">
            <video id="myVideo" autoplay playsinline muted></video>
            <div id="wave-log">ℹ️ कुरुक्षेत्र की तरह लाइव देखने और सुनने के लिए नोड कनेक्ट करें...</div>
        </div>
       
        <div style="display: flex; gap: 10px; justify-content: center;">
            <input type="text" id="frequencyInput" placeholder="विचार तरंगें भेजें (Type Thought)...">
            <button onclick="transmitWave()">प्रसारित करें</button>
        </div>
    </div>

    <script>
        let socket;
        async function activateDrishti() {
            let id = document.getElementById('nodeId').value;
            if(!id) return alert('कृपया अपनी दिव्य पहचान ID डालें!');
           
            // 👁️ बिना ऐप के सीधे ब्राउज़र से कैमरा एक्सेस करना (लाइव देखने के लिए)
            try {
                const stream = await navigator.mediaDevices.getUserMedia({ video: true, audio: false });
                const videoElement = document.getElementById('myVideo');
                videoElement.srcObject = stream;
            } catch (err) {
                alert("कैमरा एक्सेस नहीं मिल सका, लेकिन ऑडियो/टेक्स्ट सिमुलेशन चालू रहेगा।");
            }

            // स्थानीय नोड नेटवर्क से जुड़ना
            socket = new WebSocket(`ws://127.0.0.1:8000/ws/${id}`);
           
            socket.onmessage = function(event) {
                let log = document.getElementById('wave-log');
                if(log.innerText.startsWith('ℹ️')) log.innerText = '';
                log.innerHTML += '<div>' + event.data + '</div>';
                log.scrollTop = log.scrollHeight;
            };
            alert('✨ दिव्य दृष्टि और लाइव कैमरा सफलतापूर्वक लिंक हो गए हैं!');
        }

        function transmitWave() {
            let input = document.getElementById('frequencyInput');
            if(input.value) {
                socket.send(input.value);
                input.value = '';
            }
        }
    </script>
</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
async def get_interface():
    return HTMLResponse(HTML_INTERFACE)

@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: str):
    await telepathy_engine.connect_node(websocket)
    try:
        await telepathy_engine.transmit_wave("सिस्टम चेतना", f"🟢 [नोड: {client_id}] लाइव देखने/सुनने के नेटवर्क में आ गया है।")
        while True:
            data = await websocket.receive_text()
            await telepathy_engine.transmit_wave(client_id, data)
    except WebSocketDisconnect:
        telepathy_engine.disconnect_node(websocket)
        await telepathy_engine.transmit_wave("सिस्टम चेतना", f"🔴 [नोड: {client_id}] नेटवर्क तरंगों से बाहर चला गया।")

if __name__ == "__main__":
    print("✨ दिव्य दृष्टि लाइव इंजन सक्रिय हो रहा है...")
    webbrowser.open("http://127.0.0.1:8000")
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="error")
 
