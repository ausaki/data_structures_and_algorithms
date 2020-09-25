# title: count-square-submatrices-with-all-ones
# detail: https://leetcode.com/submissions/detail/393727288/
# datetime: Thu Sep 10 20:34:13 2020
# runtime: 664 ms
# memory: 15.9 MB

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        result = 0
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    continue
                matrix[i][j] = min(matrix[i][j - 1], matrix[i - 1][j] , matrix[i - 1][j - 1]) + 1
                result += matrix[i][j]
        return result + sum(matrix[0]) + sum(matrix[i][0] for i in range(1, m))