# title: stream-of-characters
# detail: https://leetcode.com/submissions/detail/400496025/
# datetime: Fri Sep 25 16:50:02 2020
# runtime: 652 ms
# memory: 37.4 MB

class TrieTree:
    END = '#'

    def __init__(self):
        self.root = {}
    
    def add(self, s):
        node = self.root
        for c in s:
            if c not in node:
                node[c] = {}
            node = node[c]
        node[self.END] = self.END
    
    def search(self, s):
        node = self.root
        for c in s:
            if c not in node:
                return False
            node = node[c]
            if self.END in node:
                return True

class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = TrieTree()
        self.maxsize = 0
        for w in words:
            self.trie.add(reversed(w))
            self.maxsize = max(self.maxsize, len(w))
        self.q = collections.deque()
        self.size = 0
    
    def query(self, letter: str) -> bool:
        self.q.appendleft(letter)
        self.size += len(letter)
        while self.size > self.maxsize:
            self.size -= len(self.q.pop())
        return self.trie.search(self.q)
    

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)