from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHTTPRequestHandler (BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content type', 'text/html')
        self.end_headers()
        path = self.path
        try:
            with open(path[1:], 'rb') as file:
                content = file.read()
            self.wfile.write(content)
        except IOError:
            self.send_error(404, "File not found")

port = 8080
server = ('', port)
httpd = HTTPServer(server, SimpleHTTPRequestHandler)
print("Server Started...")
httpd.serve_forever()
        