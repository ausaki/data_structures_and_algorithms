# title: count-square-submatrices-with-all-ones
# detail: https://leetcode.com/submissions/detail/393700408/
# datetime: Thu Sep 10 18:43:06 2020
# runtime: 1496 ms
# memory: 18 MB

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        result = 0
        for i in range(m):
            for j in range(n):
                o = matrix[i][j] == 1
                matrix[i][j] += (matrix[i][j - 1] if j else 0) + (matrix[i - 1][j] if i else 0) - (matrix[i - 1][j - 1] if i and j else 0)
                if not o:
                    continue
                sz0, sz1 = 0, min(i, j)
                while sz0 <= sz1:
                    k = (sz0 + sz1) // 2
                    t = i - k - 1
                    l = j - k - 1
                    s = matrix[i][j] - (matrix[i][l] if l >= 0 else 0) - (matrix[t][j] if t >= 0 else 0) + (matrix[t][l] if t >= 0 and l >= 0 else 0)
                    if s == (k + 1) ** 2:
                        sz0 = k + 1
                    else:
                        sz1 = k - 1
                result += sz1 + 1
        return result