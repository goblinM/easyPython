# -*- encoding=utf-8 -*-
"""
created by goblinM 2019-08-06
source: python3-cookbook
字典的一些操作:
defaultdict
OrderDict
zip
"""
from collections import defaultdict
from collections import OrderedDict
from operator import itemgetter


class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id)


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

    def test_zip(self):
        prices = {
            'ACME': 45.23,
            'AAPL': 612.78,
            'IBM': 205.55,
            'HPQ': 37.20,
            'FB': 10.75
        }
        min_price = min(zip(prices.values(), prices.keys()))  # 查找字典中最小值
        # 普通做法：
        min_price_c = prices[min(prices, key=lambda k: prices[k])]
        max_price = max(zip(prices.values(), prices.keys()))  # 查找字典中最大值
        # 普通做法：
        max_price_c = prices[max(prices, key=lambda k: prices[k])]
        print("min_price=", min_price)
        print("min_price_c=", min_price_c)
        print("max_price=", max_price)
        print("max_price_c=",max_price_c)

    def test_itemgetter(self):
        rows = [
            {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
            {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
            {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
            {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
        ]
        rows_by_fname = sorted(rows, key=itemgetter('fname'))
        rows_by_fname_lambda = sorted(rows, key=lambda x: x["fname"])
        rows_by_uid = sorted(rows, key=itemgetter('uid'))
        rows_by_uid_lambda = sorted(rows, key=lambda x: x["uid"])
        rows_by_multiple = sorted(rows, key=itemgetter('fname', 'uid'))
        rows_by_multiple_lambda = sorted(rows, key=lambda x: (x['fname'], x['uid']))
        print("rows_by_fname=",rows_by_fname)
        print("rows_by_uid=",rows_by_uid)
        print("rows_by_fname_lambda=",rows_by_fname_lambda)
        print("rows_by_uid_lambda=",rows_by_uid_lambda)
        print("rows_by_multiple=",rows_by_multiple)
        print("rows_by_multiple_lambda=",rows_by_multiple_lambda)

    def sort_not_compare(self):
        users = [User(23), User(3), User(99)]
        print(users)
        # 方法一：lambda
        print(sorted(users, key=lambda u: u.user_id))

        # 方法二：operator.attrgetter
        from operator import attrgetter
        print(sorted(users, key=attrgetter('user_id')))


if __name__ == "__main__":
    b = TestDict()
    b.common_dict()
    b.collection_dict()
    b.compare_dict()
    b.order_dict()
    b.test_zip()
    b.test_itemgetter()
    b.sort_not_compare()
