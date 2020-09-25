# title: minimum-moves-to-reach-target-with-rotations
# detail: https://leetcode.com/submissions/detail/395529837/
# datetime: Mon Sep 14 17:32:13 2020
# runtime: 260 ms
# memory: 15.9 MB

class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        m = n = len(grid)
        visited = {(1, 0)}
        q = collections.deque([(1, 0)])
        moves = 0
        while q:
            for _ in range(len(q)):
                p, k = q.popleft()
                i, j = divmod(p, n)
                if i == n - 1 and j == n - 1 and k == 0:
                    return moves    
                if k == 0:
                    next = (p + 1, k)
                    if j + 1 < n and grid[i][j + 1] != 1 and next not in visited:
                        q.append(next)
                        visited.add(next)
                    if i + 1 < m and grid[i + 1][j] != 1 and grid[i + 1][j - 1] != 1:
                        next = (p + n, k)
                        if next not in visited:
                            q.append(next)
                            visited.add(next)
                        next = (p + n - 1, 1)
                        if next not in visited:
                            q.append(next)
                            visited.add(next)
                else:
                    next = (p + n, k)
                    if i + 1 < m and grid[i + 1][j] != 1 and next not in visited:
                        q.append(next)
                        visited.add(next)
                    if j + 1 < n and grid[i][j + 1] != 1 and grid[i - 1][j + 1] != 1:
                        next = (p + 1, k)
                        if next not in visited:
                            q.append(next)
                            visited.add(next)
                        next = (p - n + 1, 0)
                        if next not in visited:
                            q.append(next)
                            visited.add(next)
            moves += 1
        return -1
