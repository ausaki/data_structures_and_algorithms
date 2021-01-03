# title: maximum-xor-with-an-element-from-array
# detail: https://leetcode.com/submissions/detail/435011020/
# datetime: Sun Dec 27 12:00:24 2020
# runtime: 9240 ms
# memory: 260.5 MB

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
        self.root = Node()
    
    def find_max_xor(self, x):
        curr = self.root
        bits = getbits(x)
        for b in bits:
            if curr.child[1 - b] is not None:
                curr = curr.child[1 - b]
            else:
                curr = curr.child[b]
            if curr is None:
                break
        return (x ^ curr.value) if curr else -1
    
    def add(self, x):
        curr = self.root
        bits = getbits(x)
        for b in bits:
            if curr.child[b] is None:
                curr.child[b] = Node()
            curr = curr.child[b]
        curr.value = x
        

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
            
                
        
        