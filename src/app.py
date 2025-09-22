from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

def build_message(query_params):
    name = query_params.get("name", [None])[0]
    if name:
        return f"Hi {name},\nHow are you?"
    else:
        return "Hello, World!"

class HelloWorldHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_url = urlparse(self.path)
        if parsed_url.path == "/":
            query_params = parse_qs(parsed_url.query)
            response = build_message(query_params)

            self.send_response(200)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(response.encode("utf-8"))
        else:
            self.send_response(404)
            self.end_headers()

def run(server_class = HTTPServer, handler_class = HelloWorldHandler, port = 8000):
    server = server_class(("", port), handler_class)
    print(f"Hello World API is serving on port {port}")
    server.serve_forever()

if __name__ == "__main__":
    run()
