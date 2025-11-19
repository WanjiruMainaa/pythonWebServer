# import module
from http.server import BaseHTTPRequestHandler, HTTPServer

class ServerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Hello, world!")

if __name__ == "__main__":
    server = HTTPServer(('', 8000), ServerHandler)
    print("Server running on http://localhost:8000")
    server.serve_forever()
