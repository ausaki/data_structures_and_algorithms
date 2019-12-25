# title: diagonal-traverse
# detail: https://leetcode.com/submissions/detail/286630751/
# datetime: Tue Dec 17 21:42:41 2019
# runtime: 204 ms
# memory: 15.3 MB

class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        M = len(matrix)
        if M == 0:
            return []
        N = len(matrix[0])
        res = []
        for c in range(M + N - 1):
            r = range(max(0, c - M + 1), min(c, N - 1) + 1)
            if c % 2:
                r = reversed(r)
            for x in r:
                res.append(matrix[c - x][x])
        return res