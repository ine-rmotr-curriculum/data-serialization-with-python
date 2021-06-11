#!/usr/bin/env python
from http.server import BaseHTTPRequestHandler, HTTPServer
from time import asctime

class Server(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('X-INE-Course', 'HTTP using Python')
        self.end_headers()
        self.wfile.write(f"<h3>Request details:</h3>\n".encode())
        self.wfile.write(f"<p>You accessed path: {self.path}</p>\n".encode())
        self.wfile.write(b"<blockquote><pre>\n")
        self.wfile.write(f"{self.requestline}\n{self.headers}".encode())
        self.wfile.write(b"</pre></blockquote>\n")

host, port = "0.0.0.0", 2504
server = HTTPServer((host, port), Server)

print(f"{asctime()} Server Start: ({host}:{port})")
try:
    server.serve_forever()
except KeyboardInterrupt:
    server.server_close()
print(f"{asctime()} Server Stop")