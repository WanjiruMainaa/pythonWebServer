# pythonWebServer
A collaborative project that involves creating a simple HTTP server using python.

steps
-importing the server model 
'''
-from http.server 
'''
-handle http on server and create istance on the server
''''
-import BaseHTTPRequestHandler, HTTPServer
class serverHandler(BaseHTTPRequestHandler)'''
''
-class serverHandler(BaseHTTPRequestHandler):

''''
 This custom request handler class allows us to handle different request methods like GET, POST, and so on.
''''
-handle status code ok
-set the header to be html type
- end the header
- The last part of the code defines the function that starts the server
- remote location to be port 8000
