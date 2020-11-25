from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import os

data = {'result': 'this is a test'}

class Resquest(BaseHTTPRequestHandler):
    def do_GET(self):
        #print(self.path)
        self.send_response(200)
        fn = os.path.join(os.getcwd(),"WEB",self.path.replace("/",os.sep)[1:])
        #print(os.path.isfile(fn),fn)
        if(os.path.isfile(fn)):
            self.send_response(200)
            self.send_header("Content-type","text/html;charset=UTF-8")
            self.end_headers()
            self.wfile.write(open(fn,'rb').read())
        else:
            self.send_response(404)
            # self.send_header('Content-type', 'application/json')
            # self.end_headers()
            # self.wfile.write(json.dumps(data).encode())
    def log_message(self, format, *args):
        return

class Server():
    def __init__(self,host= 'localhost',port= 8888):
        config = (host,port)
        server = HTTPServer(config, Resquest)
        print("Starting server, listen at: %s:%s" % config)
        server.serve_forever()
        return server