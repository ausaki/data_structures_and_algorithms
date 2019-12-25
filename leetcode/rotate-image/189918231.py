# title: rotate-image
# detail: https://leetcode.com/submissions/detail/189918231/
# datetime: Fri Nov 16 18:25:34 2018
# runtime: 28 ms
# memory: N/A

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        N = len(matrix)
        for i in range(N // 2 + 1):
            left = i
            top = i
            right = N - i - 1
            bottom = N - i - 1
            for _ in range(right - left):
                tmp = matrix[top][left]
                for m in range(top, bottom):
                    matrix[m][left] = matrix[m + 1][left]
                for n in range(left, right):
                    matrix[bottom][n] = matrix[bottom][n + 1]
                for m in range(bottom, top, -1):
                    matrix[m][right] = matrix[m - 1][right]
                for n in range(right, left, -1):
                    matrix[top][n] = matrix[top][n - 1]
                matrix[top][n] = tmp                