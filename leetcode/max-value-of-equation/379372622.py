# title: max-value-of-equation
# detail: https://leetcode.com/submissions/detail/379372622/
# datetime: Tue Aug 11 22:02:03 2020
# runtime: 1240 ms
# memory: 59.8 MB

import heapq
import collections

class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        # heap = []
        # result = float('-inf')
        # n = len(points)
        # for x, y in points:
        #     while heap and x - heap[0][1] > k:
        #         heapq.heappop(heap)
        #     if heap:
        #         result = max(result, x + y - heap[0][0])
        #     heapq.heappush(heap, (x - y, x))
        # return result
        q = collections.deque()
        result = float('-inf')
        n = len(points)
        for x, y in points:
            while q and x - q[0][1] > k:
                q.popleft()
            if q:
                result = max(result, x + y + q[0][0])
            i = y - x
            while q and i > q[-1][0]:
                q.pop()
            q.append((i, x))
        return result
            