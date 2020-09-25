# title: min-cost-to-connect-all-points
# detail: https://leetcode.com/submissions/detail/398689546/
# datetime: Mon Sep 21 17:35:01 2020
# runtime: 1128 ms
# memory: 78.8 MB

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        result = 0
        m = 0
        q = [(0, 0)]
        visited = [0] * n
        while m < n:
            w, i = heapq.heappop(q)
            if visited[i]:
                continue
            visited[i] = 1
            for j in range(n):
                if visited[j]:
                    continue
                ww = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                heapq.heappush(q, (ww, j))
            m += 1
            result += w
        return result