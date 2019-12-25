# title: map-sum-pairs
# detail: https://leetcode.com/submissions/detail/288227981/
# datetime: Tue Dec 24 20:55:27 2019
# runtime: 28 ms
# memory: 12.7 MB

class TrieTree:
    END = '#'
    PREFIX = '*'

    def __init__(self):
        self.root = {}
    
    def add(self, s, val):
        stack = [self.root]
        for c in s:
            if c not in stack[-1]:
                stack[-1][c] = {}
            stack.append(stack[-1][c])
        end_node = stack[-1]
        diff = val - end_node.get(self.END, 0)
        end_node[self.END] = val
        while stack:
            node = stack.pop()
            node[self.PREFIX] = node.get(self.PREFIX, 0) + diff
    
    def prefixsum(self, prefix):
        node = self.root
        for c in prefix:
            if c not in node:
                return 0
            node = node[c]
        return node[self.PREFIX]

    
class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = TrieTree()

    def insert(self, key: str, val: int) -> None:
        self.trie.add(key, val)        

    def sum(self, prefix: str) -> int:
        return self.trie.prefixsum(prefix)


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)