# title: min-cost-to-connect-all-points
# detail: https://leetcode.com/submissions/detail/398694711/
# datetime: Mon Sep 21 17:56:47 2020
# runtime: 816 ms
# memory: 17.1 MB

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        result = 0
        m = 0
        q = [(0, 0)]
        visited = [10 ** 9] * n
        while m < n:
            w, i = heapq.heappop(q)
            # print(j, i, w)
            if visited[i] < 0:
                continue
            visited[i] = -1
            for j in range(n):
                if j == i or visited[j] < 0:
                    continue
                ww = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                if ww < visited[j]:
                    visited[j] = ww
                    heapq.heappush(q, (ww, j))
            m += 1
            result += w
        return result