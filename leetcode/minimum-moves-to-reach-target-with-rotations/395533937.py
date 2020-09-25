# title: minimum-moves-to-reach-target-with-rotations
# detail: https://leetcode.com/submissions/detail/395533937/
# datetime: Mon Sep 14 17:48:26 2020
# runtime: 556 ms
# memory: 16.5 MB

class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        m = n = len(grid)
        visited = {(1, 0)}
        q = collections.deque([(1, 0)])
        moves = 0
        while q:
            for _ in range(len(q)):
                h, t = q.popleft()
                ti, tj = divmod(t, n)
                hi, hj = divmod(h, n)
                if hi == n - 1 and hj == n - 1 and ti == n - 1:
                    return moves
                for di, dj in [[0, 1], [1, 0]]:
                    hii = hi + di
                    hjj = hj + dj
                    tii = ti + di
                    tjj = tj + dj
                    if hii < n and hjj < n and tii < n and tjj < n and grid[hii][hjj] != 1 and grid[tii][tjj] != 1:
                        next = (hii * n + hjj, tii * n + tjj)
                        if hii == hjj == tii == n - 1:
                            return moves + 1
                        if next not in visited:
                            q.append(next)
                            visited.add(next)
                        if di == 1 and hi == ti:
                            next = (h + n - 1, t)
                            if next not in visited:
                                q.append(next)
                                visited.add(next)
                        if dj == 1 and hj == tj:
                            next = (h - n + 1, t)
                            if next not in visited:
                                q.append(next)
                                visited.add(next)
            moves += 1
        return -1
