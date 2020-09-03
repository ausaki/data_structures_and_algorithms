# title: queries-on-a-permutation-with-key
# detail: https://leetcode.com/submissions/detail/384025926/
# datetime: Fri Aug 21 12:27:51 2020
# runtime: 92 ms
# memory: 13.9 MB

class FenwickTree:
    def __init__(self, data) -> None:
        self.bit = None
        self._build(data)
    
    def _build(self, data):
        n = len(data) + 1
        self.bit = [0] * n
        for i in range(1, n):
            for j in range(i, i & (i - 1), -1):
                self.bit[i] += data[j - 1]
    
    def add(self, i, delta):
        i += 1
        while i < len(self.bit):
            self.bit[i] += delta
            i += i & -i
    def sum(self, i):
        i += 1
        s = 0
        while i > 0:
            s += self.bit[i]
            i &= i - 1
        return s

    def range_sum(self, l, r):
        return self.sum(r + 1) - self.sum(l)

class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        indices = [0] * m + [1] * m
        idxmap = {i: i + m - 1 for i in range(1, m + 1)}
        fw = FenwickTree(indices)
        result = []
        curr = m - 1
        for q in queries:
            i = idxmap[q]
            j = fw.sum(i - 1)
            result.append(j)
            idxmap[q] = curr
            fw.add(i, -1)
            fw.add(curr, 1)
            curr -= 1
        return result
        