# title: swim-in-rising-water
# detail: https://leetcode.com/submissions/detail/412539890/
# datetime: Sat Oct 24 17:19:29 2020
# runtime: 120 ms
# memory: 14.3 MB

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        q = [(grid[0][0], 0)]
        dist = [math.inf] * (n * n)
        dist[0] = grid[0][0]
        while q:
            d, p = heapq.heappop(q)
            if d > dist[p]:
                continue
            i, j = divmod(p, n)
            if p == n * n - 1:
                return d
            for di, dj in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
                ii, jj = i + di, j + dj
                if 0 <= ii < n and 0 <= jj < n:
                    d1 = max(grid[ii][jj], d)
                    p = ii * n + jj
                    if d1 < dist[p]:
                        dist[p] = d1
                        heapq.heappush(q, (d1, p))
            