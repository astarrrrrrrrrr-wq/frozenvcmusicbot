from http.server import BaseHTTPRequestHandler, HTTPServer
import os

class WebhookHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Bot is alive!")

    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()

    def do_POST(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Post request received")

# ✅ Rename the function here
def keep_alive():
    port = int(os.environ.get("PORT", 8080))
    server = HTTPServer(("", port), WebhookHandler)
    print(f"✅ HTTP server running on port {port}")
    server.serve_forever()

# This part is optional, only needed for standalone testing
if __name__ == "__main__":
    keep_alive()
