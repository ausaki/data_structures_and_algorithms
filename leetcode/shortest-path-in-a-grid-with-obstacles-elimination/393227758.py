# title: shortest-path-in-a-grid-with-obstacles-elimination
# detail: https://leetcode.com/submissions/detail/393227758/
# datetime: Wed Sep  9 18:15:04 2020
# runtime: 52 ms
# memory: 13.9 MB

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        if k >= m - 1 + n - 2:
            return m + n - 2
        visited = {0: k}
        dij = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        q = collections.deque([(0, k)])
        steps = 0
        while q:
            for _ in range(len(q)):
                p, k = q.popleft()
                i, j = divmod(p, n)
                if i == m - 1 and j == n - 1:
                    return steps
                for di, dj in dij:
                    ii, jj = i + di, j + dj
                    if 0 <= ii < m and 0 <= jj < n:
                        kk = k - grid[ii][jj]
                        if kk < 0:
                            continue
                        t = ii * n + jj
                        if t not in visited or kk > visited[t]:
                            q.append((t, kk))
                            # visited.setdefault(t, set()).add(kk)
                            visited[t] = kk
            steps += 1   
        return -1
