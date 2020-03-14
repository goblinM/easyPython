# -*- encoding=utf-8 -*-
"""
created by goblinM 2019-08-06
source: python3-cookbook
使用heapq构造优先队列
"""
import heapq


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        """
        (-priority, index, item) 的元组。
        优先级为负数的目的是使得元素按照优先级从高到低排序。 这个跟普通的按优先级从低到高排序的堆排序恰巧相反
        index 变量的作用是保证同等优先级元素的正确排序
        :param item:
        :param priority:
        :return:
        """
        print((-priority, self._index, item))
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)


if __name__ == '__main__':
    q = PriorityQueue()
    q.push(Item('foo'), 1)
    q.push(Item('bar'), 5)
    q.push(Item('spam'), 4)
    q.push(Item('grok'), 1)
    q.pop()
