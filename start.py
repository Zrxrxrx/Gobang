from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import os

data = {'result': 'this is a test'}
host = ('localhost', 8888)

class Resquest(BaseHTTPRequestHandler):
    def do_GET(self):
        print(self.path)
        self.send_response(200)
        fn = os.path.join(os.getcwd(),"WEB",self.path.replace("/",os.sep)[1:])
        print(os.path.isfile(fn),fn)
        if(os.path.isfile(fn)):
            self.send_header("Content-type","text/html;charset=UTF-8")
            self.end_headers()
            self.wfile.write(open(fn,'rb').read())
        else:
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(data).encode())

if __name__ == '__main__':
    server = HTTPServer(host, Resquest)
    print("Starting server, listen at: %s:%s" % host)
    server.serve_forever()