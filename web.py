from http.server import HTTPServer, BaseHTTPRequestHandler
content = """    
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TCP/IP Protocol Suite Simulator</title>
    <style>
        :root {
            --primary: #2c3e50;
            --accent: #e74c3c;
            --bg: #f8f9fa;
            --layer-bg: #ffffff;
        }

        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            background-color: var(--bg);
            color: var(--primary);
            margin: 0;
            padding: 20px;
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        .container {
            max-width: 800px;
            width: 100%;
            background: var(--layer-bg);
            padding: 30px;
            border-radius: 12px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        }

        h1 {
            text-align: center;
            margin-bottom: 30px;
            font-size: 24px;
        }

        .controls {
            display: flex;
            justify-content: center;
            margin-bottom: 30px;
        }

        button {
            background-color: var(--accent);
            color: white;
            border: none;
            padding: 12px 24px;
            font-size: 16px;
            font-weight: bold;
            border-radius: 6px;
            cursor: pointer;
            transition: background 0.2s ease;
        }

        button:hover {
            background-color: #c0392b;
        }

        .stack {
            display: flex;
            flex-direction: column;
            gap: 15px;
            position: relative;
        }

        .layer {
            border: 2px solid #e2e8f0;
            border-radius: 8px;
            padding: 20px;
            background: #fff;
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
        }

        .layer.active {
            border-color: var(--accent);
            background-color: #fffaf0;
            transform: scale(1.02);
        }

        .layer-title {
            font-weight: bold;
            font-size: 18px;
            margin-bottom: 5px;
            display: flex;
            justify-content: space-between;
        }

        .layer-protocols {
            font-size: 12px;
            color: #7f8c8d;
            text-transform: uppercase;
            letter-spacing: 1px;
        }

        .layer-desc {
            font-size: 14px;
            color: #555;
            margin-top: 8px;
        }

        .packet {
            position: absolute;
            width: 20px;
            height: 20px;
            background-color: var(--accent);
            border-radius: 50%;
            left: 30px;
            top: -40px;
            opacity: 0;
            transition: all 0.8s cubic-bezier(0.4, 0, 0.2, 1);
            z-index: 10;
            box-shadow: 0 0 10px rgba(231, 76, 60, 0.5);
        }
    </style>
</head>
<body>

<div class="container">
    <h1>TCP/IP 4-Layer Protocol Simulator</h1>
    
    <div class="controls">
        <button id="sendBtn">Transmit Data Packet</button>
    </div>

    <div class="stack">
        <div id="packet" class="packet"></div>

        <!-- Application Layer -->
        <div class="layer" id="layer4">
            <div class="layer-title">
                <span>4. Application Layer</span>
                <span class="layer-protocols">HTTP, FTP, SMTP, DNS</span>
            </div>
            <div class="layer-desc">Generates the raw payload data (e.g., website request or email content).</div>
        </div>

        <!-- Transport Layer -->
        <div class="layer" id="layer3">
            <div class="layer-title">
                <span>3. Transport Layer</span>
                <span class="layer-protocols">TCP, UDP</span>
            </div>
            <div class="layer-desc">Encapsulates data with source/destination ports. TCP ensures reliable, sequenced delivery via a handshake.</div>
        </div>

        <!-- Internet Layer -->
        <div class="layer" id="layer2">
            <div class="layer-title">
                <span>2. Internet Layer</span>
                <span class="layer-protocols">IP, ICMP, ARP</span>
            </div>
            <div class="layer-desc">Attaches the source and destination IP addresses to route packets across logical networks.</div>
        </div>

        <!-- Network Access Layer -->
        <div class="layer" id="layer1">
            <div class="layer-title">
                <span>1. Network Access Layer</span>
                <span class="layer-protocols">Ethernet, Wi-Fi, MAC</span>
            </div>
            <div class="layer-desc">Converts packets into frames and manages the physical transmission over hardware media.</div>
        </div>
    </div>
</div>

<script>
    const sendBtn = document.getElementById('sendBtn');
    const packet = document.getElementById('packet');
    const layers = [
        document.getElementById('layer4'),
        document.getElementById('layer3'),
        document.getElementById('layer2'),
        document.getElementById('layer1')
    ];

    sendBtn.addEventListener('click', () => {
        sendBtn.disabled = true;
        animatePipeline(0);
    });

    function animatePipeline(step) {
        if (step >= layers.length) {
            // Reset simulation after finishing
            setTimeout(() => {
                packet.style.opacity = '0';
                packet.style.top = '-40px';
                layers.forEach(l => l.classList.remove('active'));
                sendBtn.disabled = false;
            }, 1000);
            return;
        }

        // Highlight active architectural layer
        layers.forEach(l => l.classList.remove('active'));
        layers[step].classList.add('active');

        // Move the physical packet element dynamically
        const layerTop = layers[step].offsetTop;
        const layerHeight = layers[step].offsetHeight;
        
        packet.style.opacity = '1';
        packet.style.top = (layerTop + (layerHeight / 2) - 10) + 'px';

        setTimeout(() => {
            animatePipeline(step + 1);
        }, 1200);
    }
</script>

</body>
</html>

    """
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',880)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()