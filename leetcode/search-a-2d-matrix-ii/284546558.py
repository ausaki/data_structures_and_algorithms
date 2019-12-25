# title: search-a-2d-matrix-ii
# detail: https://leetcode.com/submissions/detail/284546558/
# datetime: Sun Dec  8 20:58:04 2019
# runtime: 40 ms
# memory: 17.4 MB

import bisect
class Solution:
    def searchMatrix(self, matrix, target):
        M = len(matrix)
        if M == 0:
            return False
        N = len(matrix[0])
        if N == 0:
            return False
        row = 0
        col = N - 1
        while row < M and col>= 0:
            val = matrix[row][col]
            if val == target:
                return True
            if val < target:
                row += 1
            else:
                col -= 1
        return False
        
        