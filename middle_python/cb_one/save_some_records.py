# -*- encoding=utf-8 -*-
"""
created by goblinM 2019-06-18
source: python3-cookbook
1.3 保留最后N个元素
1.4 查找最大或最小的N个元素
这里的一些知识点：
    1.collections: https://docs.python.org/zh-cn/3/library/collections.html
    2.heapq: https://docs.python.org/3.6/library/heapq.html
"""
import heapq
from collections import deque


class SaveRecord:
    def __init__(self):
        pass

    def save_last(self, lines, pattern, history=5):
        print(lines)
        print(pattern)
        previous_lines = deque(maxlen=history)  # 构造长度为5的双向队列
        for line in lines:
             print(line)
             if pattern in line:
                 yield line, previous_lines
             previous_lines.append(line)
        return previous_lines

    def find_max_min(self):
        nums = [1, 3, 5, 2, 45, 23, 10, 46, 9]
        print(heapq.nlargest(3, nums))
        print(heapq.nsmallest(3, nums))
        # 接受一个关键字参数
        portfolio = [
            {'name': 'IBM', 'shares': 100, 'price': 91.1},
            {'name': 'AAPL', 'shares': 50, 'price': 543.22},
            {'name': 'FB', 'shares': 200, 'price': 21.09},
            {'name': 'HPQ', 'shares': 35, 'price': 31.75},
            {'name': 'YHOO', 'shares': 45, 'price': 16.35},
            {'name': 'ACME', 'shares': 75, 'price': 115.65}
        ]
        cheap = heapq.nsmallest(3, portfolio, key=lambda x: x['price'])
        expensive = heapq.nlargest(3, portfolio, key=lambda x: x['price'])
        print(cheap)
        print(expensive)


if __name__ == '__main__':
    obj = SaveRecord()
    lines = """life is short, use python,
I think python is interesting,
the most popular language is python.
someone asked: why to learn python
not why!!!
just do it.
python is funny
python is easy"""
    pattern = 'python'
    obj.save_last(lines, pattern)
    obj.find_max_min()

