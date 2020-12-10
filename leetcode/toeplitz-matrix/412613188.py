# title: toeplitz-matrix
# detail: https://leetcode.com/submissions/detail/412613188/
# datetime: Sat Oct 24 23:25:44 2020
# runtime: 104 ms
# memory: 14.1 MB

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                ii, jj = i - j, 0
                if ii < 0:
                    ii, jj = 0, -ii
                if matrix[ii][jj] != matrix[i][j]:
                    return False
        return True
        