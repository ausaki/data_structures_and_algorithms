# title: queries-on-a-permutation-with-key
# detail: https://leetcode.com/submissions/detail/384026666/
# datetime: Fri Aug 21 12:29:42 2020
# runtime: 80 ms
# memory: 14.2 MB

class Fenwick:
    def __init__(self, n):
        sz = 1
        while sz <= n:
            sz *= 2
        self.size = sz
        self.data = [0] * sz

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.data[i]
            i -= i & -i
        return s

    def add(self, i, x):
        while i < self.size:
            self.data[i] += x
            i += i & -i

class Solution(object):
    def processQueries(self, queries, n):
        fenw = Fenwick(2 * n)
        vimap = {}
        for i in range(1, n + 1):
            fenw.add(i + n, 1)
            vimap[i] = i + n
        cur = n
        
        ans = []
        for q in queries:
            i = vimap.pop(q)
            rank = fenw.sum(i-1)
            ans.append(rank)
            
            vimap[q] = cur
            fenw.add(i, -1)
            fenw.add(cur, 1)
            cur -= 1
        return ans