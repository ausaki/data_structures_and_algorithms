# title: shortest-bridge
# detail: https://leetcode.com/submissions/detail/403857178/
# datetime: Sat Oct  3 17:48:42 2020
# runtime: 564 ms
# memory: 17.4 MB

class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        n = len(A)
        zeros = set()
        def dfs(i, j):
            A[i][j] = 2
            for di, dj in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
                ii, jj = i + di, j + dj
                if 0 <= ii < n and 0 <= jj < n:
                    if A[ii][jj] == 1:
                        dfs(ii, jj)
                    elif A[ii][jj] == 0:
                        zeros.add((ii * n + jj))
        for i in range(n):
            for j in range(n):
                if A[i][j] == 1:
                    dfs(i, j)
                    break
            else:
                continue
            break
        
        result = 2 * n
        # print(zeros)
        q = collections.deque(zeros)
        for p in zeros:
            i, j = divmod(p, n)
            A[i][j] = -1
        steps = 1
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
                            A[ii][jj] = -1
                        if A[ii][jj] == 1:
                            result = min(result, steps)
            steps += 1
        return result            
                