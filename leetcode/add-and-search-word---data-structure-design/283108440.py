# title: add-and-search-word---data-structure-design
# detail: https://leetcode.com/submissions/detail/283108440/
# datetime: Mon Dec  2 12:04:32 2019
# runtime: 296 ms
# memory: 23.7 MB

class Trie:
    def __init__(self):
        self.root = {}
    
    def add(self, word):
        node = self.root
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        node['*'] = word
        
    def search(self, word):
        def dfs(node, i):
            if i == len(word):
                return '*' in node 
            if word[i] == '.':
                for char, next_node in node.items():
                    if char == '*':
                        continue
                    if dfs(next_node, i + 1):
                        return True
                return False
            if word[i] not in node:
                return False
            return dfs(node[word[i]], i + 1)
        
        node = self.root
        return dfs(node, 0)
        
                
        
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = Trie()
        

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        self.trie.add(word)
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        return self.trie.search(word)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)