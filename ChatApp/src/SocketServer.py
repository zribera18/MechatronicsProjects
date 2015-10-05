'''
Created on Oct 1, 2015

@author: Zach
'''
import socket
import base64
from threading import Thread
import sys

HOST = 'localhost'
PORT = 8888
BUFSIZE = 1024
ADDR = (HOST, PORT)

tcpServerSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # internet socket, streaming socket
tcpServerSock.bind(ADDR)
tcpServerSock.listen(50)

while True:
    print 'Waiting for connection....'
    tcpClientSock, addr = tcpServerSock.accept()
    print '\nConnected from: ', addr
    try :
        encodedData = base64.standard_b64encode(b'Um hello, welcome to the chat room!')
        tcpClientSock.send(encodedData)
    except :
    # broken socket connection
        tcpClientSock.close()

    def recv():
        while True:
            data = tcpClientSock.recv(BUFSIZE)
            decodedData = base64.standard_b64decode(data)
            if not data: sys.exit(0)
            print '\n<<' + decodedData
        
    Thread(target = recv).start()
    while True:
        data = raw_input('')
        if not data:
            break
        encodedData = base64.standard_b64encode(data)
        tcpClientSock.sendall(encodedData)
        
    tcpClientSock.close()
tcpServerSock.close()
