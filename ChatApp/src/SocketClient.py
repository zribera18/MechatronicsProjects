'''
Created on Oct 1, 2015

@author: Zach
'''
import socket
import sys
from threading import Thread
import base64
import json
import time

HOST = 'localhost'
PORT = 8888
BUFSIZE = 1024
ADDR = (HOST, PORT)
tcpClientSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
CONNECTION = False
try:
    tcpClientSock.connect(ADDR)
except :
    print 'Unable to connect'
    
def recv():
    while True:
        data = tcpClientSock.recv(BUFSIZE)
        decodedData = base64.standard_b64decode(data)
        if not data: 
            sys.exit(0)
        print '\n<< ' + decodedData
Thread(target = recv).start() 
time.sleep(1)
while True:
    sys.stdout.flush(); sys.stdout.write('[Me] ')
    clientInput = raw_input('')
    if not True:
        break                  
    jsonData = json.dumps([{"IP":(str(tcpClientSock.getpeername()))},{"Message":(clientInput)}])
    encodedData = base64.standard_b64encode(jsonData)
    tcpClientSock.send(encodedData)

tcpClientSock.close()

# def send():
#     while True:
#         sys.stdout.write('[Me] '); sys.stdout.flush()
#         clientInput = raw_input('')
#         if not data:
#             break                  
#         jsonData = json.dumps([{"IP":(str(tcpClientSock.getpeername()))},{"Message":(clientInput)}])
#         encodedData = base64.standard_b64encode(jsonData)
#         tcpClientSock.send(encodedData)
# Thread(target = send).start()
# 
# while True:
#     data = tcpClientSock.recv(BUFSIZE)
#     decodedData = base64.standard_b64decode(data)
#     if not data: 
#         sys.exit(0)
#     print '\n<< ' + decodedData
# 
# tcpClientSock.close()