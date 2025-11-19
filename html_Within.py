# import the server
from http.server import BaseHTTPRequestHandler, HTTPServer

# place the class
html = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Hello, world!</title>
</head>
<body>
<h1>Hello, world!</h1>
<p>This is group one starting project.</p>
</body>
</html>
"""
class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        # encoe using utf-8 since it is binary
        self.wfile.write(html.encode())

if __name__ == "__main__":
    server = HTTPServer(("localhost", 8080), Handler)
    print("Server started http://localhost:8080")
    server.serve_forever()

