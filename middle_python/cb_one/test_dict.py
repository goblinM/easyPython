# -*- encoding=utf-8 -*-
"""
created by goblinM 2019-08-06
source: python3-cookbook
字典的一些操作:
defaultdict
"""
from collections import defaultdict
from collections import OrderedDict

class TestDict(object):
    def common_dict(self):
        d = {}
        d.setdefault('a', []).append(1)
        d.setdefault('a', []).append(2)
        d.setdefault('b', []).append(4)
        print(d)

        dd = {}
        dd.setdefault('a', 1)
        dd.setdefault('a', 2)
        dd.setdefault('b', 4)
        print(dd)

    def collection_dict(self):
        d = defaultdict(list)
        d['a'].append(1)
        d['a'].append(2)
        d['b'].append(4)
        print(d)

    def compare_dict(self):
        test = ["goblinM", "23", "girl"]
        # 普通做法
        d = {}
        for index, value in enumerate(test):
            if index not in d:
                d[index] = []
            d[index].append(value)
        print("d=", d)

        # defaultdict 做法
        dd = defaultdict(list)
        for index, value in enumerate(test):
            dd[index].append(value)

        print("defaultdict dd=",dd)

    def order_dict(self):
        d = OrderedDict()
        d['foo'] = 1
        d['bar'] = 2
        d['spam'] = 3
        d['grok'] = 4
        # Outputs "foo 1", "bar 2", "spam 3", "grok 4"
        for key in d:
            print(key, d[key])
        print(d)



if __name__ == "__main__":
    b = TestDict()
    b.common_dict()
    b.collection_dict()
    b.compare_dict()
    b.order_dict()
