from prometheus_client import start_http_server, Gauge
import time
import http.server

REQUEST_IN_PROGRESS = Gauge('request_inprogress',"Number of live requests on application")
REQUEST_LAST_EXECUTED = Gauge('request_last_served','Time the application was last served')

class HandleRequest(http.server.BaseHTTPRequestHandler):
    
    @REQUEST_IN_PROGRESS.track_inprogress()
    def do_GET(self):
        # REQUEST_IN_PROGRESS.inc()
        time.sleep(5)
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        self.wfile.write(bytes('<html><h2>Welcome to our first prometheus course</h2></html>','utf-8'))
        self.wfile.close
        REQUEST_LAST_EXECUTED.set_to_current_time()
        # REQUEST_LAST_EXECUTED.set(time.time())
        # REQUEST_IN_PROGRESS.dec()

if __name__ == "__main__":
    start_http_server(5001)
    server = http.server.HTTPServer(('localhost',5000), HandleRequest)
    server.serve_forever()