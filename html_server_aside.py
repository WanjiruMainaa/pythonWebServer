# import the server
from http.server import BaseHTTPRequestHandler, HTTPServer

# include the file
html = r"index.html"
with open(html, "rb") as f:
    index = f.read()
# place the class

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        # encode using utf-8 since it is binary
        self.wfile.write(index)

# initiate the local host id
if __name__ == "__main__":
    server = HTTPServer(("localhost", 8080), Handler)
    print("Server started http://localhost:8080")
    server.serve_forever()

