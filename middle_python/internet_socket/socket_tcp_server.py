# -*- encoding=utf-8 -*-
"""
使用socketserver，tcpserver和StreamRequestHandler,创建一个时间戳tcp服务器
"""
from socketserver import (TCPServer as TCP,
                          StreamRequestHandler as SRH)
from time import ctime

HOST = '127.0.0.1'
PORT = 21570
ADDR = (HOST, PORT)


class MyRequestHandler(SRH):
    # 重写StreamRequestHandler的handle方法
    # 接收到客户端的消息，调用handle方法
    def handle(self):
        print("... connected from ", self.client_address)
        write_data = '[%s] %s' % (ctime(), self.rfile.readline())
        self.wfile.write(write_data.encode())

tcpSer = TCP(ADDR, MyRequestHandler)
print('waiting for connecting...')
tcpSer.serve_forever()
