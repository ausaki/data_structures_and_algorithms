# title: search-a-2d-matrix-ii
# detail: https://leetcode.com/submissions/detail/284546566/
# datetime: Sun Dec  8 20:58:12 2019
# runtime: 28 ms
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
        
        