# title: maximum-number-of-events-that-can-be-attended
# detail: https://leetcode.com/submissions/detail/387168500/
# datetime: Fri Aug 28 00:07:51 2020
# runtime: 1356 ms
# memory: 58.8 MB

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        heap = []
        d = -1
        result = 0
        for s, e in events:
            while s > d and heap:
                ee = heapq.heappop(heap)
                if ee >= d:
                    result += 1
                    d += 1
            if s <= d:
                heapq.heappush(heap, e)
            else:
                d = s + 1
                result += 1                
        while heap:
            e = heapq.heappop(heap)
            if e >= d:
                result += 1
                d += 1
        return result