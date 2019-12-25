# title: replace-words
# detail: https://leetcode.com/submissions/detail/287735729/
# datetime: Sun Dec 22 19:10:40 2019
# runtime: 64 ms
# memory: 26.7 MB

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
        return self.END in node

    def prefix(self, s):
        prefix = ''
        node = self.root
        for c in s:
            if self.END in node:
                return prefix
            if c not in node:
                return False
            prefix += c
            node = node[c]
        if self.END in node:
            return prefix
        return ''
    
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = TrieTree()
        for word in dictionary:
            trie.add(word)
        sentence = sentence.split(' ')
        for i, word in enumerate(sentence):
            prefix = trie.prefix(word)
            if prefix:
                sentence[i] = prefix
        return ' '.join(sentence)