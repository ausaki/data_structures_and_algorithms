# title: maximum-xor-of-two-numbers-in-an-array
# detail: https://leetcode.com/submissions/detail/280082855/
# datetime: Tue Nov 19 17:44:49 2019
# runtime: 1044 ms
# memory: 152 MB

class TrieNode:
    def __init__(self):
        self.value = None
        self.next = None
    
    def next(self, v):
        if self.next is None:
            return None
        if v in self.next:
            return self.next[v]
        else:
            return None
    
    def add(self, v):
        if self.next is None:
            self.next = {}
        return self.next.setdefault(v, TrieNode())
        
class TrieTree:
    def __init__(self):
        self.root = TrieNode()
    
    def add(self, value):
        curr = self.root
        for v in value:
            curr = curr.add(v)
        curr.value = value
        
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        trie = TrieTree()
        for n in nums:
            v = bin(n)[2:]
            v = '0' * (32 - len(v)) + v
            trie.add(v)
        root = trie.root
        t1 = None
        t2 = None
        while root.next and t1 is None and t2 is None:
            if '0' in root.next and '1' in root.next:
                t1 = root.next['0']
                t2 = root.next['1']
                break
            if '0' in root.next:
                root = root.next['0']
            else:
                root = root.next['1']
        if t1 is None and t2 is None:
            return 0
        return self._find(t1, t2)
    
    def _find(self, t1, t2):
        if t1.next is None and t2.next is None:
            return int(t1.value, 2) ^ int(t2.value, 2)
        v1 = 0
        v2 = 0
        if '0' in t1.next and '1' in t2.next:
            v1 = self._find(t1.next['0'], t2.next['1'])
        if '1' in t1.next and '0' in t2.next:
            v2 = self._find(t1.next['1'], t2.next['0'])
        if v1 != 0 or v2 != 0:
            return max(v1, v2)
        if '1' in t1.next and '1' in t2.next:
            v1 = self._find(t1.next['1'], t2.next['1'])
        if '0' in t1.next and '0' in t2.next:
            v2 = self._find(t1.next['0'], t2.next['0'])
        return max(v1, v2)        
        
            
        
                
        