# title: short-encoding-of-words
# detail: https://leetcode.com/submissions/detail/409091575/
# datetime: Thu Oct 15 23:44:47 2020
# runtime: 164 ms
# memory: 16.1 MB

class TrieTree:
    END = '#'

    def __init__(self):
        self.root = {}
    
    def add(self, s):
        node = self.root
        for c in s:
            node = node.setdefault(c, {})
        node[self.END] = self.END
    
    def is_prefix(self, prefix):
        node = self.root
        for c in prefix:
            if c not in node:
                return False
            node = node[c]
        return len(node) > 1

class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words = set(words)
        tr = TrieTree()
        for w in words:
            tr.add(w[::-1])
        return sum(len(w) + 1 for w in words if not tr.is_prefix(w[::-1]))
