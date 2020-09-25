# title: coloring-a-border
# detail: https://leetcode.com/submissions/detail/400186394/
# datetime: Fri Sep 25 00:42:48 2020
# runtime: 144 ms
# memory: 14.1 MB

class Solution:
    def colorBorder(self, grid: List[List[int]], r0: int, c0: int, color: int) -> List[List[int]]:
        C = grid[r0][c0]
        if color == C: return grid
        m, n = len(grid), len(grid[0])
        q = collections.deque([r0 * n + c0])
        visited = {q[0]}
        while q:
            p = q.popleft()
            i, j = divmod(p, n)
            border = False
            for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                ii, jj = i + di, j + dj
                if 0 <= ii < m and 0 <= jj < n and (grid[ii][jj] == C or grid[ii][jj] == -1):
                    p = ii * n + jj
                    if p not in visited:
                        visited.add(p)
                        q.append(p)
                else:
                    border = True
            if border:
                grid[i][j] = -1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == -1:
                    grid[i][j] = color
        return grid
            