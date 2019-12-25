# title: 01-matrix
# detail: https://leetcode.com/submissions/detail/286874547/
# datetime: Wed Dec 18 21:26:15 2019
# runtime: 592 ms
# memory: 15.4 MB

class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        # pos = [[1, 0], [-1, 0], [0, -1], [0, 1]]
        # def dis(i, j):
        #     if 
        M = len(matrix)
        if M == 0:
            return []
        N = len(matrix[0])
        D = M + N
        res = [[D] * N for i in range(M)]
        for i in range(M):
            for j in range(N):
                if matrix[i][j] == 0:
                    res[i][j] = 0
                else:
                    if i - 1 >= 0:
                        res[i][j] = res[i - 1][j] + 1
                    if j - 1 >= 0:
                        res[i][j] = min(res[i][j - 1] + 1, res[i][j])
        for i in range(M - 1, -1, -1):
            for j in range(N - 1, -1, -1):
                if matrix[i][j] == 0:
                    res[i][j] = 0
                else:
                    if i + 1 < M:
                        res[i][j] = min(res[i + 1][j] + 1, res[i][j])
                    if j + 1 < N:
                        res[i][j] = min(res[i][j + 1] + 1, res[i][j])
        return res