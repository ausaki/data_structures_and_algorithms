# title: 01-matrix
# detail: https://leetcode.com/submissions/detail/286876564/
# datetime: Wed Dec 18 21:43:43 2019
# runtime: 748 ms
# memory: 16.3 MB

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
        seen = set()
        for i in range(M):
            for j in range(N):
                if matrix[i][j] == 0:
                    res[i][j] = 0
                    queue.append(i * N + j)
        level = 0
        while queue:
            for _ in range(len(queue)):
                k = queue.popleft()
                i, j = divmod(k, N)
                if level < res[i][j]:
                    res[i][j] = level
                for di, dj in pos:
                    ii, jj = i + di, j + dj
                    k = ii * N + jj
                    if k not in seen and 0 <= ii < M and 0 <= jj < N and matrix[ii][jj] == 1:
                        seen.add(k)
                        queue.append(k)
            level += 1
        return res