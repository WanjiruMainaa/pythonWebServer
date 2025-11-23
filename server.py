# import BaseHTTPServer
from http.server import BaseHTTPRequestHandler, HTTPServer
import os

class RequestHandler(BaseHTTPRequestHandler):
    

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
        
        # Error handling page
        Error_Page = """\
            <html>
            <body>
            <h1>Error accessing {path}</h1>
            <p>{msg}</p>
            </body>
            </html>
            """

        def handle_error(self, msg):
            content = self.Error_Page.format(path=self.path, msg=msg)
            self.send_content(content)
            
        # Handle unknown objects.
        def handle_error(self, msg):
            content = self.Error_Page.format(path=self.path, msg=msg)
            self.send_content(content, 404)

         # Send actual content.
        def send_content(self, content, status=200):
            self.send_response(status)
            self.send_header("Content-type", "text/html")
            self.send_header("Content-Length", str(len(content)))
            self.end_headers()
            self.wfile.write(content)




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

class case_no_file(object):
    '''File or directory does not exist.'''

    def test(self, handler):
        return not os.path.exists(handler.full_path)

    def act(self, handler):
        raise Exception("'{0}' not found".format(handler.path))


class case_existing_file(object):
    '''File exists.'''

    def test(self, handler):
        return os.path.isfile(handler.full_path)

    def act(self, handler):
        handler.handle_file(handler.full_path)

class case_always_fail(object):
    '''Base case if nothing else worked.'''

    def test(self, handler):
        return True

    def act(self, handler):
        raise Exception("Unknown object '{0}'".format(handler.path))

#--------------------------------------------------------
class ServerException(Exception):
    """Exception for internal server errors."""
    pass

class RequestHandler(BaseHTTPRequestHandler):
    """
    If the requested path maps to a file, that file is served.
    If anything goes wrong, an error page is constructed.
    """

    Cases = [case_no_file(),
             case_existing_file(),
             case_always_fail()]

    # How to display an error.
    Error_Page = """\
<html>
<body>
<h1>Error accessing {path}</h1>
<p>{msg}</p>
</body>
</html>
"""

    # How to display a directory listing.
    Listing_Page = '''\
<html>
<body>
<ul>
{0}
</ul>
</body>
</html>
'''

    # Classify and handle request.
    def do_GET(self):
        try:
            # Figure out what exactly is being requested.
            self.full_path = os.getcwd() + self.path

            # Figure out how to handle it.
            for case in self.Cases:
                if case.test(self):
                    case.act(self)
                    break

        # Handle errors.
        except Exception as msg:
            self.handle_error(msg)

    # Handle unknown objects.
    def handle_error(self, msg):
        content = self.Error_Page.format(path=self.path, msg=msg)
        self.send_content(content, 404)

    # Send actual content.
    def send_content(self, content, status=200):
        self.send_response(status)
        self.send_header("Content-type", "text/html")
        self.send_header("Content-Length", str(len(content)))
        self.end_headers()
        self.wfile.write(content)

    def list_dir(self, full_path):
        """Generate a directory listing."""
        try:
            entries = os.listdir(full_path)
            bullets = ['<li><a href="{0}">{0}</a></li>'.format(e)
                      for e in entries if not e.startswith('.')]
            page = self.Listing_Page.format('\n'.join(bullets))
            self.send_content(page)
        except OSError as msg:
            msg = "'{0}' cannot be listed: {1}".format(self.path, msg)
            self.handle_error(msg)

# CGI script handling here


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
