# -*- encoding=utf-8 -*-
"""
创建一个TCP服务器，接受来自客户端的消息，并返回加了时间戳前缀的相同消息
"""
from socket import *
from time import ctime

HOST = '127.0.0.1'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)  # 最大的连接数

while True:
    print("waiting for connection....")
    tcpCliSock, addr = tcpSerSock.accept()
    print("...connnected from:", addr)

    while True:
        data = tcpCliSock.recv(BUFSIZ).decode('utf-8')
        if not data or data == 'exit':
            break
        senddata = '[%s] %s' % (bytes(ctime(), encoding='utf8'), data)
        tcpCliSock.send(senddata.encode())
    tcpCliSock.close()
tcpSerSock.close()
