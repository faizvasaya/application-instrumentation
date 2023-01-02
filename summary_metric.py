from prometheus_client import start_http_server, Summary
import time
import http.server

REQUEST_LATENCY_TIME = Summary('request_latency_time', 'Time taken by each request to serve')

class HandleRequest(http.server.BaseHTTPRequestHandler):
    
    @REQUEST_LATENCY_TIME.time()
    def do_GET(self):
        # startTime = time.time()
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        self.wfile.write(bytes('<html><h2>Welcome to our first prometheus course</h2></html>','utf-8'))
        self.wfile.close
        time.sleep(1)
        # endTime = time.time() - startTime
        # REQUEST_LATENCY_TIME.observe(endTime)

if __name__ == "__main__":
    start_http_server(5001)
    server = http.server.HTTPServer(('localhost',5000), HandleRequest)
    server.serve_forever()