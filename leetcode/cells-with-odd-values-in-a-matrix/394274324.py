# title: cells-with-odd-values-in-a-matrix
# detail: https://leetcode.com/submissions/detail/394274324/
# datetime: Sat Sep 12 01:28:46 2020
# runtime: 44 ms
# memory: 13.9 MB

class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        rows = [0] * n
        cols = [0] * m
        for i, j in indices:
            rows[i] ^= 1
            cols[j] ^= 1
        c = sum(cols)
        return sum(m - c if rows[i] else c for i in range(n))
                