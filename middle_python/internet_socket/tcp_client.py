# -*- endcoding=utf-8 -*-
"""
创建TCP的客户端
"""
from socket import *

HOST = '127.0.0.1'  # ipv6的时候使用::1
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)  # ipv6的时候使用AF_INET6
tcpCliSock.connect(ADDR)
while True:
    data = input('> ')
    if not data:
        break
    tcpCliSock.send(data.encode())
    data = tcpCliSock.recv(BUFSIZ)
    if not data or data == 'exit':
        break
    print(data.decode('utf-8'))

tcpCliSock.close()
