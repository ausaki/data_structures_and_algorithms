# title: shortest-bridge
# detail: https://leetcode.com/submissions/detail/403859445/
# datetime: Sat Oct  3 17:58:45 2020
# runtime: 376 ms
# memory: 17.5 MB

class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        def dfs(i, j):
            A[i][j] = 2
            z = False
            for di, dj in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
                ii, jj = i + di, j + dj
                if 0 <= ii < n and 0 <= jj < n:
                    if A[ii][jj] == 1:
                        dfs(ii, jj)
                    elif A[ii][jj] == 0:
                        z = True
            if z:
                q.append(i * n + j)
        
        n = len(A)
        q = collections.deque()
        for i in range(n):
            for j in range(n):
                if A[i][j] == 1:
                    dfs(i, j)
                    break
            else:
                continue
            break
        steps = 0
        while q:
            for _ in range(len(q)):
                p = q.popleft()
                i, j = divmod(p, n)
                for di, dj in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
                    ii, jj = i + di, j + dj
                    if 0 <= ii < n and 0 <= jj < n:
                        p = ii * n + jj
                        if A[ii][jj] == 0:
                            q.append(p)
                            A[ii][jj] = 2
                        if A[ii][jj] == 1:
                            return steps
            steps += 1
                