# title: lucky-numbers-in-a-matrix
# detail: https://leetcode.com/submissions/detail/385695348/
# datetime: Mon Aug 24 23:19:14 2020
# runtime: 156 ms
# memory: 14 MB

class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        rows = [1e6] * m
        cols = [0] * n
        for i in range(m):
            for j in range(n):
                rows[i] = min(rows[i], matrix[i][j])
                cols[j] = max(cols[j], matrix[i][j])
        # print(rows, cols)
        return list(set(rows) & set(cols))