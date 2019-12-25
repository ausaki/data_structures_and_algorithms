# title: map-sum-pairs
# detail: https://leetcode.com/submissions/detail/288225271/
# datetime: Tue Dec 24 20:30:09 2019
# runtime: 44 ms
# memory: 12.8 MB

class TrieTree:
    END = '#'

    def __init__(self):
        self.root = {}
    
    def add(self, s, val):
        node = self.root
        for c in s:
            if c not in node:
                node[c] = {}
            node = node[c]
        node[self.END] = val
    
    def prefixsum(self, prefix):
        def _sum(node):
            if isinstance(node, int):
                return node
            return sum(_sum(next_node) for k, next_node in node.items())
        node = self.root
        for c in prefix:
            if c not in node:
                return 0
            node = node[c]
        return _sum(node)

    
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