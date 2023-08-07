import socket
from requests import get
from simple_websocket_server import WebSocketServer, WebSocket
import socketserver
import simple_http_server
import urllib
import http.server
PORT = 9097

def check_ip():
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)
    print("Your Computer Name is:" + hostname)
    print("Your Computer IP Address is:" + IPAddr)
    ip = get('https://api.ipify.org').content.decode('utf8')
    print('My public IP address is: {}'.format(ip))

class MyProxy(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        url=self.path[1:]
        self.send_response(200)
        self.end_headers()
        self.copyfile(urllib.urlopen(url), self.wfile)
        self.copyfile(urllib.urlopen(url), self.wfile)

httpd = socketserver.ThreadingTCPServer(('', PORT), MyProxy)
print("Now serving at :"+str(PORT))
httpd.serve_forever()


