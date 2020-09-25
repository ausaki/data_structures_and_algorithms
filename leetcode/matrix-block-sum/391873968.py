# title: matrix-block-sum
# detail: https://leetcode.com/submissions/detail/391873968/
# datetime: Sun Sep  6 23:49:34 2020
# runtime: 104 ms
# memory: 14.7 MB

class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        for i in range(m):
            for j in range(n):
                mat[i][j] += (mat[i][j - 1] if j else 0) + (mat[i - 1][j] if i else 0) - (mat[i - 1][j - 1] if i and j else 0)
        result = [[0] * n for i in range(m)]
        for i in range(m):
            for j in range(n):
                t = max(i - K, 0)
                b = min(i + K, m - 1)
                l = max(j - K, 0)
                r = min(j + K, n - 1)
                result[i][j] = mat[b][r] - (mat[b][l - 1] if l else 0) - (mat[t - 1][r] if t else 0) + (mat[t - 1][l - 1] if t and l else 0)
        return result
                