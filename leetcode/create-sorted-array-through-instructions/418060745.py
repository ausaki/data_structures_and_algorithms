# title: create-sorted-array-through-instructions
# detail: https://leetcode.com/submissions/detail/418060745/
# datetime: Sun Nov  8 18:47:14 2020
# runtime: 5884 ms
# memory: 29.1 MB

MOD = 10 ** 9 + 7

class FenwickTree:
    def __init__(self) -> None:
        self.bit = None
    
    def from_data(self, data):
        n = len(data) + 1
        self.bit = [0] * n
        for i in range(1, n):
            for j in range(i, i & (i - 1), -1):
                self.bit[i] += data[j - 1]
    def from_empty(self, n):
        self.bit = [0] * (n + 1)
        
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
        return self.sum(r) - self.sum(l - 1)


class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        n = len(instructions)
        fw = FenwickTree()
        m = max(instructions) + 1
        fw.from_empty(m)
        cost = 0
        for i in instructions:
            fw.add(i, 1)
            cost = (cost + min(fw.sum(i - 1), fw.range_sum(i + 1, m - 1))) % MOD
        return cost