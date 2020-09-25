# title: min-cost-to-connect-all-points
# detail: https://leetcode.com/submissions/detail/398684998/
# datetime: Mon Sep 21 17:14:33 2020
# runtime: 1052 ms
# memory: 82.2 MB

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        elements = [-1] * n
        
        def find(elements, i):
            while elements[i] >= 0:
                i = elements[i]
            return i
        
        def union(elements, i, j):
            i = find(elements, i)
            j = find(elements, j)
            if i == j:
                return False
            if elements[i] <= elements[j]:
                if elements[i] == elements[j]:
                    elements[i] -= 1
                elements[j] = i
            else:
                elements[i] = j
            return True
        
        edges = []
        for i in range(n - 1):
            for j in range(i + 1, n):
                heapq.heappush(edges, (abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]), i, j))
        result = 0
        m = n
        while m > 1:
            w, i, j = heapq.heappop(edges)
            if not union(elements, i, j):
                continue
            m -= 1
            result += w
        return result