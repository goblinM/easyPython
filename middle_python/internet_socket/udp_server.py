# -*- encoding=utf-8 -*-
"""
创建一个udp服务器，接受来自客户端的消息，并返回加了时间戳前缀的相同消息
udp不面向连接
"""
from socket import *
from time import ctime

HOST = '127.0.0.1'
PORT = 21568
BUFSIZ = 1024
ADDR = (HOST, PORT)

udpSersock = socket(AF_INET, SOCK_DGRAM)
udpSersock.bind(ADDR)

while True:
    print("waiting for message...")
    data, addr = udpSersock.recvfrom(BUFSIZ)
    if not data or data == 'exit':
        break
    senddata = '[%s] %s' % (ctime(), data)
    udpSersock.sendto(senddata.encode(), addr)
    print('...received from and return to:', addr)
udpSersock.close()
