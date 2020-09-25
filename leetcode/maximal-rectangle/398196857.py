# title: maximal-rectangle
# detail: https://leetcode.com/submissions/detail/398196857/
# datetime: Sun Sep 20 14:08:48 2020
# runtime: 468 ms
# memory: 14.6 MB

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        if m == 0: return 0
        n = len(matrix[0])
        result = 0
        for i in range(m):
            for j in range(n):
                matrix[i][j] = int(matrix[i][j])
                if matrix[i][j] == 0:
                    continue
                matrix[i][j] = (matrix[i - 1][j] if i else 0)+ 1
                h = 10 ** 5
                for k in range(j, -1, -1):
                    if matrix[i][k] == 0:
                        break
                    h = min(h, matrix[i][k])
                    result = max(result, (j - k + 1) * h)
        return result