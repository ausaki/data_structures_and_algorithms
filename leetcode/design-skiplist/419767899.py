# title: design-skiplist
# detail: https://leetcode.com/submissions/detail/419767899/
# datetime: Fri Nov 13 12:15:43 2020
# runtime: 332 ms
# memory: 21.7 MB

import random

class SkipListNode:
    def __init__(self, key=None, levels=1) -> None:
        self.key = key
        self.levels = [None] * levels

class Skiplist:
    POS_INFINITY = 20001
    NEG_INFINITY = -1
    MAX_LEVEL = 16

    def __init__(self) -> None:
        self.head = SkipListNode(key=self.NEG_INFINITY, levels=self.MAX_LEVEL)
        self.tail = SkipListNode(key=self.POS_INFINITY, levels=self.MAX_LEVEL)
        for i in range(self.MAX_LEVEL):
            self.head.levels[i] = self.tail
    
    def _find(self, key):
        path = []
        level = self.MAX_LEVEL - 1
        curr = self.head
        while level >= 0:
            nxt = curr.levels[level]
            while nxt.key < key:
                curr = nxt
                nxt = curr.levels[level]
            path.append(curr)
            level -= 1
        return curr, path
    
    def add(self, key):
        curr, path = self._find(key)
        node = SkipListNode(key, self.random_level())
        for i, prev in enumerate(reversed(path)):
            if i >= len(node.levels):
                break
            prev.levels[i], node.levels[i] = node, prev.levels[i]
        
    def search(self, key):
        curr, _ = self._find(key)
        curr = curr.levels[0]
        return curr.key == key

    def erase(self, key):
        curr, path = self._find(key)
        curr = curr.levels[0]
        if curr.key != key:
            return False
        nxt = curr.levels[0]
        for i, prev in enumerate(reversed(path)):
            if i >= len(curr.levels):
                break
            prev.levels[i] = nxt
            if i >= len(nxt.levels):
                nxt.levels.append(curr.levels[i])
        return True
    
    def random_level(self):
        l = 1
        while l < self.MAX_LEVEL and random.random() > 0.5:
            l += 1
        return l
    
# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)