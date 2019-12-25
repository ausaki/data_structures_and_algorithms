# title: 01-matrix
# detail: https://leetcode.com/submissions/detail/286869717/
# datetime: Wed Dec 18 20:42:11 2019
# runtime: 932 ms
# memory: 15.6 MB

class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        pos = [[1, 0], [-1, 0], [0, -1], [0, 1]]
        def bfs(i, j):
            queue = collections.deque([i * N + j])
            seen = {i * N + j, }
            level = 0
            while queue:
                for _ in range(len(queue)):
                    k = queue.popleft()
                    i, j = divmod(k, N)
                    if matrix[i][j] == 0:
                        return level
                    for di, dj in pos:
                        ii, jj = i + di, j + dj
                        k = ii * N + jj
                        if k not in seen and 0 <= ii < M and 0 <= jj < N:
                            seen.add(k)
                            queue.append(k)
                level += 1
                
        M = len(matrix)
        if M == 0:
            return []
        N = len(matrix[0])
        
        res = [[-1] * N for i in range(M)]
        for i in range(M):
            for j in range(N):
                if matrix[i][j] == 0:
                    res[i][j] = 0
                else:
                    res[i][j] = bfs(i, j)
        return res