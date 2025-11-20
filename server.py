# import BaseHTTPServer
from http.server import BaseHTTPRequestHandler, HTTPServer
import os

class RequestHandler(BaseHTTPRequestHandler):
    '''Handle HTTP requests by returning a fixed 'page'.'''

    # Page to send back.
    Page = '''\
<html>
<body>
<p>Hello, web!</p>
</body>
</html>
'''

    # Handle a GET request.
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.send_header("Content-Length", str(len(self.Page)))
        self.end_headers()
        self.wfile.write(self.Page.encode('utf-8'))

#----------------------------------------------------------------------

if __name__ == '__main__':
    serverAddress = ('', 8080)
    server = HTTPServer(serverAddress, RequestHandler)
    print('server running on http://localhost:8080/')
    print('press Ctrl-C to stop it')
    try:      
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n Shutting down server.")
        server.server_close()

#--------------------------------------------------------
class ServerException(Exception):
    """Exception for internal server errors."""
    pass

class RequestHandler(BaseHTTPRequestHandler):

     # Default HTML page
    Default_Page = """\
        <html>
        <body>
        <p>Hello, web!</p>
        </body>
        </html>
        """


    # HTML template for error page
    Error_Page = """\
        <html>
        <body>
        <h1>Error accessing {path}</h1>
        <p>{msg}</p>
        </body>
        </html>
        """
    

    # Main GET handler
    def do_GET(self):
        try:

            if self.path == "/" or self.path == "/index.html":
                self.send_content(self.Default_Page.encode("utf-8"), status=200)
                return

            # Build safe file path
            root = os.getcwd()
            clean_path = os.path.normpath(self.path.lstrip("/"))
            full_path = os.path.join(root, clean_path)

            # If file does not exist
            if not os.path.exists(full_path):
                self.handle_error("File not found.")
                return

            # If it's a file, serve it
            if os.path.isfile(full_path):
                return self.handle_file(full_path)

            # If it is anything else
            raise ServerException(f"Unknown object '{self.path}'")
        
        # errors in server logic
        except ServerException as msg:
            self.handle_error(f"Internal server error: {msg}", status=500)
            
         # Any unexpected issue
        except Exception as msg:
            self.handle_error(f"Unexpected error: {msg}", status=500)

    # Serve an actual file from disk
    def handle_file(self, full_path):
        try:
            # Open in binary mode
            with open(full_path, "rb") as f:
                content = f.read()

            # Send file bytes
            self.send_content(content, status=200)

        except IOError as msg:
            self.handle_error(f"Could not read file: {msg}", status=500)

