import http.server
import socketserver

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cross-Origin-Opener-Policy', 'same-origin')
        self.send_header('Cross-Origin-Embedder-Policy', 'require-corp')
        self.send_header('Cross-Origin-Resource-Policy', 'cross-origin')
        super().end_headers()

# Set the port
PORT = 8080

handler_object = MyHttpRequestHandler

my_server = socketserver.TCPServer(("", PORT), handler_object)

# Start the server
print("Serving at port", PORT)
my_server.serve_forever()
