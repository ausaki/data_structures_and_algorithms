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
        

class SkipList:
    POS_INFINITY = DummyKey(True)
    NEG_INFINITY = DummyKey(False)
    MAX_LEVEL = 32

    def __init__(self) -> None:
        self.head = SkipListNode(key=self.NEG_INFINITY, levels=self.MAX_LEVEL)
        self.tail = SkipListNode(key=self.POS_INFINITY, levels=self.MAX_LEVEL)
        for i in range(self.MAX_LEVEL):
            self.head.levels[i] = self.tail
    
    def _find(self, key):
        path = []
        curr = self.head
        for level in reversed(range(self.MAX_LEVEL)):
            nxt = curr.levels[level]
            while nxt.key < key:
                curr = nxt
                nxt = curr.levels[level]
            yield curr

    def find(self, key):
        path = self._find(key)
        for curr in path:
            pass
        curr = curr.levels[0]
        return curr.value if curr.key == key else None

    def insert(self, key, value):
        path = self._find(key)
        node = SkipListNode(key, value, self.random_level())
        for i, prev in enumerate(path, 1):
            level = self.MAX_LEVEL - i
            if level >= len(node.levels):
                continue
            prev.levels[level], node.levels[level] = node, prev.levels[level]

    def remove(self, key):
        path = list(self._find(key))
        curr = path[-1].levels[0]
        if curr.key != key:
            return
        nxt = curr.levels[0]
        for level, prev in enumerate(reversed(path)):
            if level >= len(curr.levels):
                continue
            prev.levels[level] = nxt
            if level >= len(nxt.levels):
                nxt.levels.append(curr.levels[level])

    def random_level(self):
        l = 1
        while l < self.MAX_LEVEL and random.random() > 0.5:
            l += 1
        return l

    def __str__(self) -> str:
        s = []
        curr = self.head.levels[0]
        while curr is not self.tail:
            s.append(str(curr))
            curr = curr.levels[0]
        return '\n'.join(s)

sk = SkipList()
for i in range(10):
    sk.insert(i, i)
print(sk)
print('find 5:', sk.find(5))
print('remove 5')
sk.remove(5)
print(sk)