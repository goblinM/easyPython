# -*- encoding=utf-8 -*-
"""
created by goblinM 2019-06-18
source: python3-cookbook
1.1 解压序列赋值给多个变量
1.2 解压可迭代对象赋值给多个变量
"""
import time


class UnZip:
    def __init__(self):
        pass

    def one_to_one(self):
        p = [(4, 5), 'goblinM', 49, time.time()]
        x, y, z, _ = p
        print(x)
        print(y)
        print(z)

        s = "hello"
        a, b, c, d, e = s
        print(a+b)

    def one_to_two(self):
        # *号的使用，生成的是list
        record = ("goblinM", '2233965627@qq.com', '13547865932', '15625389736')
        name, email, *phone_list = record
        print(name)
        print(email)
        print(phone_list)
        # 字符串的分割
        line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
        uname, *fields, homedir, sh = line.split(":")
        print(uname)
        print(homedir)
        print(sh)
        print(fields)
        # 列表的分割
        nums = [1, 10, 7, 4, 5]
        head, *tail = nums
        print(head)
        print(tail)
        records = [
            ('foo', 1, 2),
            ('bar', 'hello'),
            ('foo', 3, 4),
        ]

        def do_foo(x, y):
            print('foo', x, y)

        def do_bar(s):
            print('bar', s)

        for tag, *args in records:
            if tag == 'foo':
                do_foo(*args)
            elif tag == 'bar':
                do_bar(*args)


if __name__ == '__main__':
    obj = UnZip()
    obj.one_to_one()
    obj.one_to_two()
