from prometheus_client import start_http_server, Counter
import http.server

REQUEST_COUNT = Counter('app_request_counts', 'Total number of HTTP requests made to the server', ['python_custom_app','endpoint'])

class HandleRequest(http.server.BaseHTTPRequestHandler):
    
    def do_GET(self):
        #REQUEST_COUNT.inc()
        REQUEST_COUNT.labels('get_function', self.path).inc()
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        self.wfile.write(bytes('<html><h2>Welcome to our first prometheus course</h2></html>','utf-8'))
        self.wfile.close

if __name__ == "__main__":
    start_http_server(5001)
    server = http.server.HTTPServer(('localhost',5000), HandleRequest)
    server.serve_forever()