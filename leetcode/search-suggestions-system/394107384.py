# title: search-suggestions-system
# detail: https://leetcode.com/submissions/detail/394107384/
# datetime: Fri Sep 11 15:30:46 2020
# runtime: 568 ms
# memory: 20.8 MB

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
                return ''
            prefix += c
            node = node[c]
        if self.END in node:
            return prefix
        return ''
    def _search_suggestions(self, node, prefix, size):
        suggestions = []
        def search(node, prefix):
            if len(suggestions) == size:
                return
            if self.END in node:
                suggestions.append(prefix)
            for c in sorted(node):
                if c == self.END:
                    continue
                search(node[c], prefix + c)
                if len(suggestions) == size:
                    return
        search(node, prefix)
        return suggestions
    
    def find_suggestions(self, keyword, size):
        result = []
        curr = self.root
        prefix = ''
        for c in keyword:
            if c not in curr:
                break
            prefix += c
            curr = curr[c]
            result.append(self._search_suggestions(curr, prefix, size))
        for i in range(len(result), len(keyword)):
            result.append([])
        return result
    
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        T = TrieTree()
        for p in products:
            T.add(p)
        return T.find_suggestions(searchWord, 3)
        
            