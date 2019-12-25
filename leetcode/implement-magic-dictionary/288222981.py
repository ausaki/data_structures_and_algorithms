# title: implement-magic-dictionary
# detail: https://leetcode.com/submissions/detail/288222981/
# datetime: Tue Dec 24 20:08:39 2019
# runtime: 32 ms
# memory: 12.8 MB

class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        

    def buildDict(self, words: List[str]) -> None:
        """
        Build a dictionary through a list of words
        """
        self.mapping = collections.defaultdict(set)
        for word in words:
            for i in range(len(word)):
                self.mapping[word[:i] + '*' + word[i + 1:]].add(word)
        print(self.mapping)
        
    def search(self, word: str) -> bool:
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        """
        for i in range(len(word)):
            w = word[:i] + '*' + word[i + 1:]
            if w in self.mapping and (word not in self.mapping[w] or len(self.mapping[w]) > 1):
                return True
        return False
        


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)