# title: maximal-square
# detail: https://leetcode.com/submissions/detail/398212633/
# datetime: Sun Sep 20 14:55:46 2020
# runtime: 212 ms
# memory: 14.4 MB

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        if m == 0: return 0
        n = len(matrix[0])
        result = 0
        for i in range(m):
            for j in range(n):
                matrix[i][j] = int(matrix[i][j])
                if matrix[i][j] == 0:
                    continue
                w = matrix[i][j] = 1 + min(matrix[i - 1][j - 1] if i and j else 0, matrix[i - 1][j] if i else 0, matrix[i][j - 1] if j else 0)
                result = max(result, w * w)
        return result