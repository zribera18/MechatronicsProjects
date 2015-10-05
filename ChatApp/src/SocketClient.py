'''
Created on Oct 1, 2015

@author: Zach
'''
import socket
import sys
from threading import Thread
import base64

HOST = 'localhost'
PORT = 8888
BUFSIZE = 1024
ADDR = (HOST, PORT)
tcpClientSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    tcpClientSock.connect(ADDR)
except :
    print 'Unable to connect'

def send():
    while True:
        data = raw_input('')
        if not data:
            break
        encodedData = base64.standard_b64encode(data)
        tcpClientSock.send(encodedData)
Thread(target = send).start()

while True:
    data = tcpClientSock.recv(BUFSIZE)
    decodedData = base64.standard_b64decode(data)
    if not data: sys.exit(0)
    print '\n<<' + decodedData

tcpClientSock.close()