# title: search-a-2d-matrix
# detail: https://leetcode.com/submissions/detail/145886017/
# datetime: Mon Mar 19 17:25:43 2018
# runtime: 40 ms
# memory: N/A

class Solution(object):
    def searchMatrix_(self, matrix, s, e, target):
        if s > e:
            return False
        m = (s + e) / 2
        i = m / self.n
        j = m % self.n
        
        if matrix[i][j] == target:
            return True
        if matrix[i][j] < target:
            return self.searchMatrix_(matrix, m + 1, e, target)
        return self.searchMatrix_(matrix, s, m - 1, target)
    
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        self.m = len(matrix)
        self.n = len(matrix[0])
        return self.searchMatrix_(matrix, 0, self.m * self.n - 1, target)
        
        