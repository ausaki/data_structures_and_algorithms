# title: rotate-image
# detail: https://leetcode.com/submissions/detail/190426832/
# datetime: Mon Nov 19 11:49:34 2018
# runtime: 24 ms
# memory: N/A

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        N = len(matrix)
        for i in range(N // 2):
            left = i
            top = i
            right = N - i - 1
            bottom = N - i - 1
            l = right - left + 1
            if l == 1:
                break
            tmp = matrix[top][left:right + 1]
            for n in range(l):
                matrix[top][left + n] = matrix[bottom - n][left]
            for n in range(l):
                matrix[top + n][left] = matrix[bottom][left + n]
            for n in range(l):
                matrix[bottom][left + n] = matrix[bottom - n][right]
            for n in range(l):
                matrix[top + n][right] = tmp[n]
            # for _ in range(right - left):
            #     tmp = matrix[top][left]
            #     for m in range(top, bottom):
            #         matrix[m][left] = matrix[m + 1][left]
            #     for n in range(left, right):
            #         matrix[bottom][n] = matrix[bottom][n + 1]
            #     for m in range(bottom, top, -1):
            #         matrix[m][right] = matrix[m - 1][right]
            #     for n in range(right, left, -1):
            #         matrix[top][n] = matrix[top][n - 1]
            #     matrix[top][n] = tmp      
            # 1 2 3
            # 4 5 6
            # 7 8 9