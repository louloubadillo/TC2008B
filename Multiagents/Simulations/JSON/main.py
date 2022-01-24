from pyngrok import ngrok
from http.server import BaseHTTPRequestHandler, HTTPServer
import logging
import json
import os
import time 
from agents import CleaningModel

#ngrok 
ngrok.install_ngrok()
ngrok.kill()
port = int(os.environ.get('PORT', 8585))
server_address = ('', port)
public_url = ngrok.connect(port="8585", proto="http", options={"bind_tls": True})
print("\n" + "#" * 94)
print(f"## Tracking URL: {public_url} ##")
print("#" * 94, end="\n\n")
ngrok.kill()

# Model execution
M = 10
N = 12
total_agents = 8
dirty_cells = 0.5
max_time = 3
start_timer = time.time()
model = CleaningModel(M, N, total_agents, dirty_cells)

# JSON
def updateFeatures():
    features = []
    model.step()
    features = model.status_agents()
    print(features)
    return features

# Post the information in `features` for each iteration
def featuresToJSON(info_list):
    featureDICT = []
    for info in info_list:
        feature = {
            "position" : info['nextPos'], # position
            "kind" : info['type'], # type
            "function" : info['function'],
            "moves" : info['moves']
            }
        featureDICT.append(feature)
    return json.dumps(featureDICT)

# This is the server. It controls the simulation.
# Server run (do not change it)
class Server(BaseHTTPRequestHandler):
    
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
    def do_GET(self):
        logging.info("GET request,\nPath: %s\nHeaders:\n%s\n", 
                     str(self.path), str(self.headers))
        self._set_response()
        self.wfile.write("GET request for {}".format(self.path).encode('utf-8'))
    
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        #post_data = self.rfile.read(content_length)
        post_data = json.loads(self.rfile.read(content_length))
        
        # If you have issues with the encoder, toggle the following lines: 
        #logging.info("POST request,\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n",
                     #str(self.path), str(self.headers), post_data.decode('utf-8'))
        logging.info("POST request,\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n",
                     str(self.path), str(self.headers), json.dumps(post_data))
        # Here, magick happens 
        # --------------------       
        features = updateFeatures()
        #print(features)
        # import pdb; pdb.set_trace()
        self._set_response()
        resp = "{\"data\":" + featuresToJSON(features) + "}"
        print(resp)
        self.wfile.write(resp.encode('utf-8'))


# Server run (do not change it)
def run(server_class=HTTPServer, handler_class=Server, port=8585):
    logging.basicConfig(level=logging.INFO)
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    public_url = ngrok.connect(port).public_url
    logging.info("ngrok tunnel \"{}\" -> \"http://127.0.0.1:{}\"".format(
        public_url, port))
    logging.info("Starting httpd...\n") # HTTPD is HTTP Daemon!
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:   # CTRL + C stops the server
        pass
    httpd.server_close()
    logging.info("Stopping httpd...\n")
run(HTTPServer, Server)