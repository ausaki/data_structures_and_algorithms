# title: diagonal-traverse
# detail: https://leetcode.com/submissions/detail/286630444/
# datetime: Tue Dec 17 21:40:07 2019
# runtime: 220 ms
# memory: 15.4 MB

class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        M = len(matrix)
        if M == 0:
            return []
        N = len(matrix[0])
        res = []
        x = 0
        for c in range(M + N - 1):
            i = max([0, c - M + 1])
            j = min([c, N - 1])
            r = range(i , j + 1)
            if c % 2:
                r = reversed(r)
            for x in r:
                res.append(matrix[c - x][x])
        return res