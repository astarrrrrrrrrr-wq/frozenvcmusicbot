import os
from http.server import HTTPServer, BaseHTTPRequestHandler
from threading import Thread

class WebhookHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"Bot is alive!")

def run_http_server():
    port = int(os.environ.get("PORT", 8080))
    server = HTTPServer(("", port), WebhookHandler)
    print(f"✅ HTTP server running on port {port}")
    server.serve_forever()

def keep_alive():
    t = Thread(target=run_http_server)
    t.start()
