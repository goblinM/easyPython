# -*- endcoding=utf-8 -*-
"""
创建udp的客户端
"""
from socket import *

HOST = '127.0.0.1'
PORT = 21568
ADDR = (HOST, PORT)
BUFSIZ = 1024

udpClisock = socket(AF_INET, SOCK_DGRAM)

while True:
    data = input('> ')
    if not data or data == 'exit':
        break
    udpClisock.sendto(data.encode(), ADDR)
    data, ADDR = udpClisock.recvfrom(BUFSIZ)
    if not data or data == 'exit':
        break
    print(data)
udpClisock.close()
