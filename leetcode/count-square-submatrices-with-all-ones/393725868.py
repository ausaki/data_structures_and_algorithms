# title: count-square-submatrices-with-all-ones
# detail: https://leetcode.com/submissions/detail/393725868/
# datetime: Thu Sep 10 20:28:48 2020
# runtime: 636 ms
# memory: 15.8 MB

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        result = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    continue
                matrix[i][j] = min(matrix[i][j - 1] if j else 0, matrix[i - 1][j] if i else 0, matrix[i - 1][j - 1] if i and j else 0) + 1
                result += matrix[i][j]
        return result