# title: cells-with-odd-values-in-a-matrix
# detail: https://leetcode.com/submissions/detail/394270990/
# datetime: Sat Sep 12 01:19:20 2020
# runtime: 44 ms
# memory: 14 MB

class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        rows = [0] * n
        cols = [0] * m
        for i, j in indices:
            rows[i] += 1
            cols[j] += 1
        return sum((rows[i] + cols[j]) % 2 for i in range(n) for j in range(m))
                