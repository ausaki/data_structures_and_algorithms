# title: maximal-rectangle
# detail: https://leetcode.com/submissions/detail/398208993/
# datetime: Sun Sep 20 14:44:43 2020
# runtime: 248 ms
# memory: 14.5 MB

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        if m == 0: return 0
        n = len(matrix[0])
        result = 0
        for i in range(m):
            stack = []
            for j in range(n):
                matrix[i][j] = int(matrix[i][j])
                if matrix[i][j] == 0:
                    stack.clear()
                    continue
                matrix[i][j] = (matrix[i - 1][j] if i else 0)+ 1
                h = matrix[i][j]
                k = j
                while stack and h <= matrix[i][stack[-1][0]]:
                    k = stack.pop()[1]
                stack.append([j, k])
                for h, k in stack:
                    result = max(result, (j - k + 1) * matrix[i][h])
        return result