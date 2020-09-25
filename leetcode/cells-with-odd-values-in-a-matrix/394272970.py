# title: cells-with-odd-values-in-a-matrix
# detail: https://leetcode.com/submissions/detail/394272970/
# datetime: Sat Sep 12 01:25:07 2020
# runtime: 36 ms
# memory: 13.9 MB

class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        rows = [0] * n
        cols = [0] * m
        for i, j in indices:
            rows[i] ^= 1
            cols[j] ^= 1
        return sum((rows[i] ^ cols[j]) for i in range(n) for j in range(m))
                