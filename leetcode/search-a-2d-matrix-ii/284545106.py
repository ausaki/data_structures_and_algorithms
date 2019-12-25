# title: search-a-2d-matrix-ii
# detail: https://leetcode.com/submissions/detail/284545106/
# datetime: Sun Dec  8 20:44:20 2019
# runtime: 24 ms
# memory: 17.3 MB

import bisect
class Solution:
    def searchMatrix(self, matrix, target):
        M = len(matrix)
        if M == 0:
            return False
        N = len(matrix[0])
        if N == 0:
            return False
        col = N
        for i in range(M):
            j = bisect.bisect(matrix[i], target, 0, col)
            if 0 <= j - 1 < col and matrix[i][j - 1] == target:
                return True
            col = j
            if col == 0:
                break
        return False
        