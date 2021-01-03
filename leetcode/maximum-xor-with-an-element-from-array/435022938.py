# title: maximum-xor-with-an-element-from-array
# detail: https://leetcode.com/submissions/detail/435022938/
# datetime: Sun Dec 27 12:35:53 2020
# runtime: 4456 ms
# memory: 160.8 MB

class Node:
    def __init__(self, value = 0):
        self.value = value
        self.child = [None] * 2

        
def getbits(x):
    b = []
    for i in reversed(range(31)):
        b.append((x >> i) & 1)
    return b


class Trie:
    def __init__(self):
        self.root = [None, None, -1]
    
    def find_max_xor(self, x):
        if self.root[0] is None and self.root[1] is None:
            return -1
        curr = self.root
        bits = getbits(x)
        for b in bits:
            if curr[1 - b] is not None: # equivalents to 2 * curr + 1 if b == 1 else 2 * curr + 2
                curr = curr[1 - b]
            else:
                curr = curr[b]
        return x ^ curr[-1]
    
    def add(self, x):
        curr = self.root
        bits = getbits(x)
        for b in bits:
            if curr[b] is None:
                curr[b] = [None, None, None]
            curr = curr[b]
        curr[-1] = x
        

class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        nums.sort()
        m = len(nums)
        n = len(queries)
        idx = sorted(range(n), key=lambda i: queries[i][1])
        res = [-1] * n
        t = Trie()
        j = 0
        for i in idx:
            while j < m and nums[j] <= queries[i][1]:
                t.add(nums[j])
                j += 1
            res[i] = t.find_max_xor(queries[i][0])
        return res
            
                
        
        