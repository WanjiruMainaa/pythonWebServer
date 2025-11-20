# import BaseHTTPServer
from http.server import BaseHTTPRequestHandler, HTTPServer
import os

class RequestHandler(BaseHTTPRequestHandler):

    """Handle HTTP requests by returning a fixed 'page'."""

    def do_GET(self):
        """Serve files based on self.path using os.getcwd(), existence check, and file check."""
        try:
            # 1. Get current working directory
            current_dir = os.getcwd()

            # 2. Build  file path from request path
            req_path = self.path.lstrip("/")  # remove leading "/"
            file_path = os.path.join(current_dir, req_path)

            # Default to index.html if root requested
            if self.path == "/" or self.path.strip() == "":
                file_path = os.path.join(current_dir, "index.html")

            # 3. Check if file exists
            if not os.path.exists(file_path):
                self.send_error_page(404, "File does not exist")
                return

            # 4. Check if it is a file
            if not os.path.isfile(file_path):
                self.send_error_page(404, "Path is not a file")
                return

            # 5. Serve the file
            self.handle_file(file_path)

        except IOError as e:
            self.send_error_page(500, f"I/O Error: {e}")

    def handle_file(self, full_path):
        """Read file in binary mode and send it with proper headers."""
        try:
            with open(full_path, 'rb') as html:
                page = html.read()

            # Determine simple content type
            if full_path.endswith(".html"):
                page_str= page.decode("utf-8")

                # the values
                values = {
                    'date_time': self.date_time_string(),
                    'client_host': self.client_address[0],
                    'client_port': self.client_address[1],
                    'command': self.command,
                    'path': self.path
                }

                page = page_str.format(**values).encode("utf-8")
                page_type = "text/html"

            elif full_path.endswith(".txt"):
                page_type = "text/plain"
            else:
                page_type = "application/octet-stream"

                # Send response headers
                self.send_response(200)
                self.send_header("Content-Type", page_type)
                self.send_header("Content-Length", str(len(page)))
                self.end_headers()

                self.wfile.write(page)
        except IOError as e:
            self.send_error_page(500, f"I/O Error: {e}")
            return




    # # Handle a GET request.
    # def send_page(self, page):
    #     self.send_response(200)
    #     self.send_header("Content-type", "text/html")
    #     self.send_header("Content-Length", str(len(page)))
    #     self.end_headers()

        def send_error_page(self, code, message):
            """Send HTML error page."""
            page = f"<h1>{code} - {message}</h1>"
            pages = page.encode('utf-8')
            self.send_response(code)
            self.send_header("Content-Type", "text/html")
            self.send_header("Content-Length", str(len(pages)))
            self.end_headers()
            self.wfile.write(pages)


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


    # Create a user-friendly error page and send correct HTTP code
    def handle_error(self, msg, status=404):
        content = self.Error_Page.format(path=self.path, msg=msg)
        self.send_content(content.encode("utf-8"), status=status)



    # Send any content to the browser
    def send_content(self, content, status=200):
        self.send_response(status)
        self.send_header("Content-Type", "text/html")
        self.send_header("Content-Length", str(len(content)))
        self.end_headers()
        self.wfile.write(content)

# Run server

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
