# -*- encoding=utf-8 -*-
"""
创建一个时间戳tcp客户端
"""
from socket import *

HOST = '127.0.0.1'
PORT = 21570
ADDR = (HOST, PORT)
BUFSIZE = 1024

while True:
    tcpCliSock = socket(AF_INET, SOCK_STREAM)
    tcpCliSock.connect(ADDR)
    data = input("> ")
    if not data or data == 'exit':
        break
    tcpCliSock.send(data.encode())
    data = tcpCliSock.recv(BUFSIZE)
    if not data or data == 'exit':
        break
    print(data.strip())
    tcpCliSock.close()
