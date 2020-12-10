# title: path-with-minimum-effort
# detail: https://leetcode.com/submissions/detail/412811925/
# datetime: Sun Oct 25 10:56:56 2020
# runtime: 780 ms
# memory: 15.1 MB

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        q = [(0, 0)]
        dist = [math.inf] * (m * n) 
        dist[0] = 0
        while q:
            d, p = heapq.heappop(q)
            if d > dist[p]:
                continue
            if p == m * n - 1:
                return d
            i, j = divmod(p, n)
            for di, dj in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
                ii, jj = i + di, j + dj
                if 0 <= ii < m and 0 <= jj < n:
                    p = ii * n + jj
                    d1 = max(d, abs(heights[i][j] - heights[ii][jj]))
                    if d1 < dist[p]:
                        dist[p] = d1
                        heapq.heappush(q, (d1, p))
        