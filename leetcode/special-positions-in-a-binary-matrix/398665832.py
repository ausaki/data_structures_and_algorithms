# title: special-positions-in-a-binary-matrix
# detail: https://leetcode.com/submissions/detail/398665832/
# datetime: Mon Sep 21 15:57:24 2020
# runtime: 172 ms
# memory: 14 MB

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        rows = [-1] * m
        cols = [0] * n
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    if rows[i] == -1:
                        rows[i] = j
                    else:
                        rows[i] = -2
                    cols[j] += 1
        return sum(1 for i in rows if i >= 0 and cols[i] == 1)
