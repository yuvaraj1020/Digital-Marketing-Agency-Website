import http.server
import socketserver
import urllib.request
import urllib.error
import urllib.parse
import sys

PORT = 8000
BACKEND_URL = "http://localhost:5000"

class VercelProxyHandler(http.server.SimpleHTTPRequestHandler):
    def proxy_request(self):
        url = BACKEND_URL + self.path
        
        # Read request body if present
        content_length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_length) if content_length > 0 else None
        
        # Filter out headers that might cause issues for the proxy request
        headers = {}
        for k, v in self.headers.items():
            if k.lower() not in ['host', 'connection', 'content-length', 'accept-encoding']:
                headers[k] = v
        
        if body:
             headers['Content-Length'] = str(len(body))

        req = urllib.request.Request(url, data=body, headers=headers, method=self.command)
        
        try:
            with urllib.request.urlopen(req) as response:
                self.send_response(response.status)
                for k, v in response.headers.items():
                    if k.lower() not in ['transfer-encoding', 'connection', 'date', 'server']:
                        self.send_header(k, v)
                self.end_headers()
                self.wfile.write(response.read())
        except urllib.error.HTTPError as e:
            self.send_response(e.code)
            for k, v in e.headers.items():
                if k.lower() not in ['transfer-encoding', 'connection', 'date', 'server']:
                    self.send_header(k, v)
            self.end_headers()
            self.wfile.write(e.read())
        except Exception as e:
            self.send_response(500)
            self.end_headers()
            self.wfile.write(str(e).encode('utf-8'))

    def do_GET(self):
        if self.path.startswith('/api/') or self.path.startswith('/auth/') or self.path.startswith('/admin/api/'):
            return self.proxy_request()
        return super().do_GET()

    def do_POST(self):
        return self.proxy_request()

    def do_PUT(self):
        return self.proxy_request()

    def do_DELETE(self):
        return self.proxy_request()

if __name__ == '__main__':
    with socketserver.TCPServer(("", PORT), VercelProxyHandler) as httpd:
        print(f"Vercel Dev Simulator running at http://localhost:{PORT}")
        print(f"Serving static files from current directory")
        print(f"Proxying /api/* and /auth/* to {BACKEND_URL}")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down.")
            sys.exit(0)
