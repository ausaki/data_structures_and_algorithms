# title: find-median-from-data-stream
# detail: https://leetcode.com/submissions/detail/344365190/
# datetime: Mon May 25 15:34:56 2020
# runtime: 372 ms
# memory: 24.8 MB

import heapq

class Heap:

    def __init__(self, min=True):
        self.heap = []
        self.last_index = -1
        if min:
            self.cmp = lambda a, b: a - b
        else:
            self.cmp = lambda a, b: b - a
        
    def insert(self, value):
        self.last_index += 1
        if self.last_index == len(self.heap):
            self.heap.append(0)
        index = self.last_index
        parent = (index - 1) // 2
        while parent >= 0 and self.cmp(self.heap[parent], value) > 0:
            self.heap[index] = self.heap[parent]
            index = parent
            parent = (index - 1) // 2
        self.heap[index] = value
    
    def push(self, value):
        self.insert(value)
        
    def pop(self):
        if self.last_index < 0:
            raise ValueError('Heap is empty')
        value = self.heap[0]
        last_value = self.heap.pop()
        self.last_index -= 1
        index = 0
        child = 2 * index + 1
        while child <= self.last_index:
            if child + 1 <= self.last_index and self.cmp(self.heap[child + 1], self.heap[child]) < 0:
                child += 1
            if self.cmp(last_value, self.heap[child]) > 0: 
                self.heap[index] = self.heap[child]
                index = child
                child = 2 * index + 1
            else:
                break
        self.heap[index] = last_value
        return value

    def peek(self):
        if self.last_index >= 0:
            return self.heap[0]
        return None
    
    def __len__(self):
        return self.last_index + 1
    
    def __getitem__(self, i):
        return self.heap[i]
    
    
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.left = Heap(False)   # maximum heap
        self.right = Heap()  # minimum heap
        

    def addNum(self, num: int) -> None:
        if len(self.left) == 0:
            self.left.insert(num)
            print(self.left.heap, self.right.heap)
            return
        
        if num > self.left[0]:
            self.right.insert(num)
            if len(self.right) - len(self.left) > 1:
                val = self.right.pop()
                self.left.insert(val)
        else:
            self.left.insert(num)
            if len(self.left) - len(self.right) > 1:
                val = self.left.pop()
                self.right.insert(val)            
        
    def findMedian(self) -> float:
        l = len(self.left)
        r = len(self.right)
        if l == r == 0:
            raise ValueError('empty stream!!!')
        if l == r:
            return (self.left[0] + self.right[0]) / 2
        if l > r:
            return self.left[0]
        return self.right[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()