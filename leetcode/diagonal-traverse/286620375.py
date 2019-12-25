# title: diagonal-traverse
# detail: https://leetcode.com/submissions/detail/286620375/
# datetime: Tue Dec 17 20:08:29 2019
# runtime: 216 ms
# memory: 15.3 MB

class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        M = len(matrix)
        if M == 0:
            return []
        N = len(matrix[0])
        res = []
        x = 0
        c = 0
        l2r = 1
        while c <= M + N - 2:
            while not (0 <= x < N and 0 <= c - x < M):
                x += l2r
            while 0 <= x < N and 0 <= c - x < M:
                res.append(matrix[c - x][x])
                x += l2r
            l2r = -l2r
            c += 1
        return res