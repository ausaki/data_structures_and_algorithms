# title: search-a-2d-matrix-ii
# detail: https://leetcode.com/submissions/detail/284543465/
# datetime: Sun Dec  8 20:28:29 2019
# runtime: 32 ms
# memory: 17.5 MB

import bisect
class Solution:
    def searchMatrix(self, matrix, target):
        M = len(matrix)
        if M == 0:
            return False
        N = len(matrix[0])
        if N == 0:
            return False
        for i in range(M):
            j = bisect.bisect(matrix[i], target)
            if 0 <= j - 1 < N and matrix[i][j - 1] == target:
                return True
        return False
        