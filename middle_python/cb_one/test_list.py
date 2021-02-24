# -*- encoding=utf-8 -*-
"""
created by goblinM 2019-08-06
source: python3-cookbook
序列的一些操作:
yield
slice
collections.Counter
"""


class TestList:
    def dedque(self, items):
        """在序列上保持元素顺序并且同时消除重复值: 值可以hashable"""
        seen = set()
        for item in items:
            if item not in seen:
                yield item
                seen.add(item)

    def dedque_two(self, items, key=None):
        """在序列上保持元素顺序并且同时消除重复值: 值不可以hashable"""
        seen = set()
        for item in items:
            val = item if key is None else key(item)
            if val not in seen:
                yield item
                seen.add(val)

    def test_slice(self):
        item = [0, 1, 2, 3, 4, 5, 6]
        a = slice(2, 4)  # 生成一个切片对象
        print(item[2:4])
        print(item[a])
        b = slice(5, 10, 2)
        print(b.start)  # 切片对象的第一个值
        print(b.stop)  # 切片对象的步子
        print(b.step)  # 切片对象的最后一个值
        s = "HelloWorld"
        print(b.indices(len(s)))  # indices(size) 方法将它映射到一个已知大小的序列上,返回一个三元组 (start, stop, step)
        for i in range(*b.indices(len(s))):
            print(s[i])

    def test_groupby(self):
        """排序后分组"""
        from operator import itemgetter
        from itertools import groupby

        rows = [
            {'address': '5412 N CLARK', 'date': '07/01/2012'},
            {'address': '5148 N CLARK', 'date': '07/04/2012'},
            {'address': '5800 E 58TH', 'date': '07/02/2012'},
            {'address': '2122 N CLARK', 'date': '07/03/2012'},
            {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
            {'address': '1060 W ADDISON', 'date': '07/02/2012'},
            {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
            {'address': '1039 W GRANVILLE', 'date': '07/04/2012'}
        ]

        rows.sort(key=itemgetter("date"))
        for date, items in groupby(rows, key=itemgetter('date')):
            print(date)
            for i in items:
                print(' ', i)

    def test_compress(self):
        addresses = [
            '5412 N CLARK',
            '5148 N CLARK',
            '5800 E 58TH',
            '2122 N CLARK',
            '5645 N RAVENSWOOD',
            '1060 W ADDISON',
            '4801 N BROADWAY',
            '1039 W GRANVILLE'
        ]
        counts = [0, 3, 10, 4, 1, 7, 6, 1]
        from itertools import compress
        more5 = [n > 5 for n in counts]
        print("more5=",more5)
        filter_address = list(compress(addresses,more5))
        print("filter_address=", filter_address)

    def test_namedtuple(self):
        # 映射名称到序列元素 collection.namedtuple
        from collections import namedtuple
        subscriber = namedtuple('subscriber', ['addr', 'joined'])  # 创建一个subscriber类型，以及addr和joined字段
        sub = subscriber('centerPark', '2011-09-12')  # 给addr, joined 赋值
        print(sub)
        print(sub.addr)
        print(sub.joined)
        # 可以索引和解压
        addr, joined = sub
        print(addr)
        print(joined)
        Stock = namedtuple('Stock', ['name', 'shares', 'price'])

        def compute_cost(records):
            total = 0.0
            for rec in records:
                print(*rec)
                s = Stock(*rec)
                total += s.shares * s.price
            return total
        # compute_cost(Stock('a','32',124))

    def test_chainmap(self):
        from collections import ChainMap
        a = {'x':1, 'y':2}
        b = {'y':2, 'z':4}
        c = ChainMap(a,b)  # 合并字典a和字典b
        print(c['x'])
        print(c['y'])
        print(c['z'])
        print(len(c))
        print(list(c.keys()))
        print(list(c.values()))
        values = ChainMap()
        values['x'] = 1
        values = values.new_child()
        values['x'] = 2
        print(values)


if __name__ == "__main__":
    obj = TestList()
    # a = [1, 5, 2, 1, 9, 1, 5, 10]
    # print(list(obj.dedque(a)))
    # b = [{'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]
    # print(list(obj.dedque_two(b,key=lambda d:(d["x"], d["y"]))))
    # obj.test_slice()
    # obj.test_groupby()
    # obj.test_namedtuple()
    obj.test_chainmap()
