# title: set-matrix-zeroes
# detail: https://leetcode.com/submissions/detail/145882381/
# datetime: Mon Mar 19 16:52:29 2018
# runtime: 163 ms
# memory: N/A

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        # 常量空间复杂度
        # 关键问题是：直接修改原 matrix，会丢失0的信息
        
        rows = len(matrix)
        cols = len(matrix[0])
        row_markers = [None] * rows
        col_markers = [None] * cols
        
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    row_markers[i] = 1
                    col_markers[j] = 1
        
        for i in range(rows):
            for j in range(cols):
                if row_markers[i] == 1 or col_markers[j] == 1:
                    matrix[i][j] = 0
        