import argparse
import sys
import string
import random
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

def id_generator(size=60, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
DEFAULT_HOST = '127.0.0.1'
DEFAULT_PORT = 9000
x=0
a=dict()
class RequestHandler(BaseHTTPRequestHandler):
  
    def do_GET(self):
        c=self.client_address[0];
        if(c in a):
            a[c]=int((a[c]+1)/2);
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
	    count=1
            while(count>0):
		    d="	Hi Client: Your Cookie I'd is : "+id_generator()
		    b=bytes(d)
		    self.wfile.write(b)
		    count=count-1
            return
        else:
            a[c]=1;
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
            
            count=1
            while(count>0):
		    d="	Hi Client: Your Cookie I'd is : "+id_generator()
		    b=bytes(d)
		    self.wfile.write(b)
		    count=count-1
            return   

class CustomHTTPServer(HTTPServer):
    def __init__(self, host, port):
        server_address = (host, port)
        HTTPServer.__init__(self, server_address, RequestHandler)
        
def run_server(port):
    try:
        server= CustomHTTPServer(DEFAULT_HOST, port)
        print ("Custom HTTP server started on port: %s" % port)
        server.serve_forever()
    except Exception as err:
        print ("Error:%s" %err)
    except KeyboardInterrupt:
        print ("Server interrupted and is shutting down...")
        server.socket.close()
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Simple HTTP Server Example')
    parser.add_argument('--port', action="store", dest="port", type=int, default=DEFAULT_PORT)
    given_args = parser.parse_args() 
    port = given_args.port
    run_server(port)
