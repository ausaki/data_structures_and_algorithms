# title: toeplitz-matrix
# detail: https://leetcode.com/submissions/detail/412611585/
# datetime: Sat Oct 24 23:19:23 2020
# runtime: 96 ms
# memory: 14.3 MB

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m, n = len(matrix), len(matrix[0])
        diagonals = {}
        for i in range(m):
            for j in range(n):
                if diagonals.setdefault(i - j, matrix[i][j]) != matrix[i][j]:
                    return False
        return True
        