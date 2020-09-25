# title: maximal-rectangle
# detail: https://leetcode.com/submissions/detail/398307669/
# datetime: Sun Sep 20 21:13:09 2020
# runtime: 224 ms
# memory: 14.4 MB

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        if m == 0: return 0
        n = len(matrix[0])
        result = 0
        for i in range(m):
            stack = []
            matrix[i].append(0)
            for j in range(n + 1):
                matrix[i][j] = int(matrix[i][j])
                h = 0
                if matrix[i][j] != 0:
                    h = matrix[i][j] = (matrix[i - 1][j] if i else 0)+ 1
                while stack and h < matrix[i][stack[-1]]:
                    hh = matrix[i][stack.pop()]
                    k = stack[-1] if stack else -1
                    result = max(result, (j - k - 1) * hh)
                stack.append(j)
        return result