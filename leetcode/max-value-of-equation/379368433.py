# title: max-value-of-equation
# detail: https://leetcode.com/submissions/detail/379368433/
# datetime: Tue Aug 11 21:49:49 2020
# runtime: 1324 ms
# memory: 59.8 MB

import heapq

class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        heap = [(points[0][0] - points[0][1], points[0][0])]
        result = float('-inf')
        n = len(points)
        for i in range(1, n):
            x, y = points[i]
            while heap and x - heap[0][1] > k:
                heapq.heappop(heap)
            if heap:
                result = max(result, x + y - heap[0][0])
            heapq.heappush(heap, (x - y, x))
        return result
            