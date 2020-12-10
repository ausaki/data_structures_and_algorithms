# title: design-skiplist
# detail: https://leetcode.com/submissions/detail/419549964/
# datetime: Thu Nov 12 21:14:37 2020
# runtime: 452 ms
# memory: 21.6 MB

import random

class SkipListNode:
    def __init__(self, key=None, levels=1) -> None:
        self.key = key
        self.levels = [None] * levels

class Skiplist:
    POS_INFINITY = 20001
    NEG_INFINITY = -1
    MAX_LEVEL = 32

    def __init__(self) -> None:
        self.head = SkipListNode(key=self.NEG_INFINITY, levels=self.MAX_LEVEL)
        self.tail = SkipListNode(key=self.POS_INFINITY, levels=self.MAX_LEVEL)
        for i in range(self.MAX_LEVEL):
            self.head.levels[i] = self.tail
    
    def add(self, key):
        path = []
        level = self.MAX_LEVEL - 1
        curr = self.head
        while level >= 0:
            while curr.levels[level].key <= key:
                curr = curr.levels[level]
            path.append(curr)
            if level == 0:
                node = SkipListNode(key, self.random_level())
                for i, prev in enumerate(reversed(path)):
                    if i >= len(node.levels):
                        break
                    prev.levels[i], node.levels[i] = node, prev.levels[i]
                break
            level -= 1
        
    def search(self, key):
        curr = self.head
        level = self.MAX_LEVEL - 1
        while level >= 0:
            while curr.levels[level].key < key:
                curr = curr.levels[level]
            if curr.levels[level].key == key:
                return True
            level -= 1
        return False

    def erase(self, key):
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