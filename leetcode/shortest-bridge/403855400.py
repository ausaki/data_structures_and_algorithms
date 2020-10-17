# title: shortest-bridge
# detail: https://leetcode.com/submissions/detail/403855400/
# datetime: Sat Oct  3 17:41:29 2020
# runtime: 608 ms
# memory: 18.2 MB

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
                        zeros.add((ii, jj))
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
        visited = {(i, j)}
        steps = 1
        while q:
            for _ in range(len(q)):
                i, j = q.popleft()
                for di, dj in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
                    ii, jj = i + di, j + dj
                    if 0 <= ii < n and 0 <= jj < n:
                        if A[ii][jj] == 0 and (ii, jj) not in visited:
                            visited.add((ii, jj))
                            q.append((ii, jj))
                        if A[ii][jj] == 1:
                            result = min(result, steps)
            steps += 1
        return result            
                