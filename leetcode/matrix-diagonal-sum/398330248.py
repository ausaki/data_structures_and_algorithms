# title: matrix-diagonal-sum
# detail: https://leetcode.com/submissions/detail/398330248/
# datetime: Sun Sep 20 22:36:22 2020
# runtime: 112 ms
# memory: 13.8 MB

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        m = len(mat)
        s = 0
        for i in range(m):
            s += mat[i][i]
            s += mat[i][m - i - 1]
        if m % 2:
            s -= mat[m// 2][m // 2]
        return s