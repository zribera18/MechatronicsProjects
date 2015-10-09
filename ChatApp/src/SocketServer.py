'''
Created on Oct 1, 2015

@author: Zach
'''
import socket
import base64
from threading import Thread
import sys
import json

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
    print '\nConnected with: ', addr
    try :
        encodedData = base64.standard_b64encode(b'Um hello, welcome to the chat room!')
        tcpClientSock.send(encodedData)
    except :
    # broken socket connection
        tcpClientSock.close()

    def recv():
        while True:
            try:
                data = tcpClientSock.recv(BUFSIZE)
                decodedData = base64.standard_b64decode(data)
                decodedJson = json.loads(decodedData)
                if decodedJson[1]["Message"] == "":
                    print "No Data"
                else:
                    print '\n<< [' + decodedJson[0]["IP"] +"] " +  decodedJson[1]["Message"]
            except:
                print '\nDisconnected with: ', addr
                tcpClientSock.close()
                sys.exit()
    Thread(target = recv).start()
    while True:
        data = raw_input('')
        if not data:
            break
        encodedData = base64.standard_b64encode(data)
        tcpClientSock.sendall(encodedData)
        
    tcpClientSock.close()
tcpServerSock.close()
