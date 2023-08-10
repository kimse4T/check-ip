import socket
from requests import get
PORT = 9097
from sys import platform

def check_ip():
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)
    print("Your Computer Name is:" + hostname)
    print("Your Computer IP Address is:" + IPAddr)
    ip = get('https://api.ipify.org').content.decode('utf8')
    print('My public IP address is: {}'.format(ip))
    print(platform)

check_ip()


