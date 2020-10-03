# title: pancake-sorting
# detail: https://leetcode.com/submissions/detail/402315202/
# datetime: Wed Sep 30 00:50:24 2020
# runtime: 40 ms
# memory: 14.2 MB

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
        return self.sum(r) - self.sum(l)
    
class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        n = len(arr)
        idx = [0] * n
        for i, j in enumerate(arr):
            idx[j - 1] = i
        ft = FenwickTree([0] * n)
        result = []
        for v in range(n, 0, -1):
            i = idx[v - 1]
            j = ft.range_sum(i, n - 1)
            k = i + j
            if k > 0:
                result.append(k)
            result.append(k + 1)
            ft.add(i, 1)
        return result            