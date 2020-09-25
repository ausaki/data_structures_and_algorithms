# title: minimum-moves-to-move-a-box-to-their-target-location
# detail: https://leetcode.com/submissions/detail/394252594/
# datetime: Sat Sep 12 00:25:28 2020
# runtime: 452 ms
# memory: 21.1 MB

class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        check = lambda i, j: 0 <= i < m and 0 <= j < n and grid[i][j] != '#'
        dist = lambda i, j: abs(i - ti) + abs(j - tj)
        
        m, n = len(grid), len(grid[0])
        dij = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        pi, pj, bi, bj = 0, 0, 0, 0
        ti, tj = 0, 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'S':
                    pi, pj = i, j
                if grid[i][j] == 'B':
                    bi, bj = i, j
                if grid[i][j] == 'T':
                    ti, tj = i, j
        for i, j in [[ti, tj], [bi, bj]]:
            k = 0
            for di, dj in dij:
                ii, jj = i + di, j + dj
                if not (0 <= ii < m and 0 <= jj < n) or grid[ii][jj] == '#':
                    k += 1
            if k == 4:
                return -1
        q = [(0, pi * n + pj, bi * n + bj)]
        visited = {(pi * n + pj, bi * n + bj)}
        pushes = 1e6
        while q:
            psh, p, b = heapq.heappop(q)
            pi, pj = divmod(p, n)
            bi, bj = divmod(b, n)
            if grid[bi][bj] == 'T':
                return psh
            for di, dj in dij:
                pii, pjj = pi + di, pj + dj
                if not check(pii, pjj):
                    continue
                if pii == bi and pjj == bj:
                    bii, bjj = bi + di, bj + dj
                    if not check(bii, bjj):
                        continue
                    if grid[bii][bjj] == 'T':
                        return psh + 1
                    st = (pii * n + pjj, bii * n + bjj)
                    if st not in visited:
                        visited.add(st)
                        heapq.heappush(q, (psh + 1, pii * n + pjj, bii * n + bjj))
                else:
                    st = (pii * n + pjj, b)
                    if st not in visited:
                        visited.add(st)
                        heapq.heappush(q, (psh, pii * n + pjj, b))
        return -1