# title: shortest-path-in-a-grid-with-obstacles-elimination
# detail: https://leetcode.com/submissions/detail/393228263/
# datetime: Wed Sep  9 18:17:28 2020
# runtime: 48 ms
# memory: 13.8 MB

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        if k >= m - 1 + n - 2:
            return m + n - 2
        if m == n == 1:
            return 0
        visited = {0: k}
        dij = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        q = collections.deque([(0, k)])
        steps = 0
        while q:
            for _ in range(len(q)):
                p, k = q.popleft()
                i, j = divmod(p, n)
                for di, dj in dij:
                    ii, jj = i + di, j + dj
                    if ii == m - 1 and jj == n - 1:
                        return steps + 1
                    if 0 <= ii < m and 0 <= jj < n:
                        kk = k - grid[ii][jj]
                        if kk < 0:
                            continue
                        t = ii * n + jj
                        if t not in visited or kk > visited[t]:
                            q.append((t, kk))
                            visited[t] = kk
            steps += 1   
        return -1
