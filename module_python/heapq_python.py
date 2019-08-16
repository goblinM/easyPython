# -*- encoding=utf-8 -*-
"""
这个是heapq模块的一些基本方法的使用
created by goblinM 2019-08-06
"""
import heapq


class HeapqTest:
    def __init__(self):
        pass

    def create_heap_one(self):
        """使用heapq.heappush()"""
        heap_list = []
        for i in range(23, 32):
            heapq.heappush(heap_list,i)
        print(heap_list[0])  # 获取最小的值
        print(heapq.heappop(heap_list) for _ in range(len(heap_list)))  # 堆排序结果

    def heap_sort(self, iterable):
        h = []
        for value in iterable:
            heapq.heappush(h, value)
        print(heapq.heappop(h) for _ in range(len(h)))


if __name__ == '__main__':
    heap = HeapqTest()
    heap.create_heap_one()
    heap.heap_sort([8, 4, 2, 5, 29, 7])


