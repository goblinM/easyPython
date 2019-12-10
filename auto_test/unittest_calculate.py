# -*- encoding=utf-8 -*-
"""
这个是unittest的单元测试所需要实现的功能
这是简单的加减乘除
"""


class Calculate:
    def __init__(self, a, b):
        self.a = int(a)
        self.b = int(b)

    def add(self):
        return self.a+self.b

    def sub(self):
        return self.a-self.b

    def mul(self):
        return self.a*self.b

    def div(self):
        return self.a/self.b
