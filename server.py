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