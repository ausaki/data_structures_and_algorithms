# title: design-skiplist
# detail: https://leetcode.com/submissions/detail/419549322/
# datetime: Thu Nov 12 21:10:53 2020
# runtime: 552 ms
# memory: 21.7 MB

import random

class SkipListNode:
    def __init__(self, key=None, value=None, levels=1) -> None:
        self.key = key
        self.value = value
        self.levels = [None] * levels

    def __str__(self) -> str:
        s = '{}: {}, levels: '.format(self.key, self.value)
        for node in self.levels:
            s += ' ' + str(node.key)
        return s

class DummyKey:
    def __init__(self, pos_infinity) -> None:
        self._dummy = pos_infinity
    
    def __eq__(self, o: object) -> bool:
        return False
    
    def __lt__(self, o) -> bool:
        return not self._dummy
    
    def __le__(self, o) -> bool:
        return not self._dummy
    
    def __gt__(self, o):
        return self._dummy
    
    def __ge__(self, o):
        return self._dummy

    def __str__(self) -> str:
        return '+Inf' if self._dummy else '-Inf'
        

class Skiplist:
    MAX_INFINITY = DummyKey(True)
    MIN_INFINITY = DummyKey(False)
    MAX_LEVEL = 32

    def __init__(self) -> None:
        self.head = SkipListNode(key=self.MIN_INFINITY, levels=self.MAX_LEVEL)
        self.tail = SkipListNode(key=self.MAX_INFINITY, levels=self.MAX_LEVEL)
        for i in range(self.MAX_LEVEL):
            self.head.levels[i] = self.tail
    
    def insert(self, key, value):
        path = []
        level = self.MAX_LEVEL - 1
        curr = self.head
        while level >= 0:
            while curr.levels[level].key <= key:
                curr = curr.levels[level]
            path.append(curr)
            if level == 0:
                node = SkipListNode(key, value, self.random_level())
                for i, prev in enumerate(reversed(path)):
                    if i >= len(node.levels):
                        break
                    prev.levels[i], node.levels[i] = node, prev.levels[i]
                break
            level -= 1
        
    def find(self, key):
        curr = self.head
        level = self.MAX_LEVEL - 1
        while level >= 0:
            while curr.levels[level].key < key:
                curr = curr.levels[level]
            if curr.levels[level].key == key:
                return curr.levels[level].value
            level -= 1
        return None

    def remove(self, key):
        path = []
        level = self.MAX_LEVEL - 1
        curr = self.head
        while level >= 0:
            while curr.levels[level].key < key:
                curr = curr.levels[level]
            path.append(curr)
            if level == 0 and curr.levels[level].key == key:
                node = curr.levels[level]
                for i, prev in enumerate(reversed(path)):
                    if i >= len(node.levels):
                        break
                    prev.levels[i] = node.levels[i]
                return True
            level -= 1
        return False
    
    def random_level(self):
        l = 1
        while random.random() > 0.5:
            l += 1
        return min(l, self.MAX_LEVEL)
    
    def search(self, target: int) -> bool:
        return self.find(target) is not None
    
    def add(self, num: int) -> None:
        self.insert(num, num)

    def erase(self, num: int) -> bool:
        return self.remove(num)
        
    def __str__(self) -> str:
        s = []
        curr = self.head.levels[0]
        while curr is not self.tail:
            s.append(str(curr))
            curr = curr.levels[0]
        return '\n'.join(s)
# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)