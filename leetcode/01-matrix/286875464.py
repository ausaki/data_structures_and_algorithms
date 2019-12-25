# title: 01-matrix
# detail: https://leetcode.com/submissions/detail/286875464/
# datetime: Wed Dec 18 21:34:42 2019
# runtime: 576 ms
# memory: 15.5 MB

class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
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
                    res[i][j] = min(res[i][j], (res[i - 1][j] + 1) if i > 0 else D, (res[i][j - 1] + 1) if j > 0 else D)
        for i in range(M - 1, -1, -1):
            for j in range(N - 1, -1, -1):
                if matrix[i][j] == 1:
                    res[i][j] = min(res[i][j], (res[i + 1][j] + 1) if i < M - 1 else D, (res[i][j + 1] + 1) if j < N - 1 else D)
        return res