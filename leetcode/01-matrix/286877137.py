# title: 01-matrix
# detail: https://leetcode.com/submissions/detail/286877137/
# datetime: Wed Dec 18 21:48:52 2019
# runtime: 764 ms
# memory: 15.6 MB

class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        pos = [[1, 0], [-1, 0], [0, -1], [0, 1]]
        M = len(matrix)
        if M == 0:
            return []
        N = len(matrix[0])
        D = M + N
        res = [[D] * N for i in range(M)]
        queue = collections.deque()
        for i in range(M):
            for j in range(N):
                if matrix[i][j] == 0:
                    res[i][j] = 0
                    queue.append(i * N + j)
        while queue:
            k = queue.popleft()
            i, j = divmod(k, N)
            for di, dj in pos:
                ii, jj = i + di, j + dj
                k = ii * N + jj
                if 0 <= ii < M and 0 <= jj < N and res[ii][jj] > res[i][j] + 1:
                    res[ii][jj] = res[i][j] + 1
                    queue.append(k)
        return res