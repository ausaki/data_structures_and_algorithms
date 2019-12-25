# title: implement-trie-(prefix-tree)
# detail: https://leetcode.com/submissions/detail/283118206/
# datetime: Mon Dec  2 12:48:43 2019
# runtime: 124 ms
# memory: 26.5 MB

class Trie:
    
    def __init__(self):
        self.root = {}
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        node['*'] = word
        
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node:
                return False
            node = node[char]
        return '*' in node
        
    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for char in prefix:
            if char not in node:
                return False
            node = node[char]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)