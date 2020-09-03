# title: cheapest-flights-within-k-stops
# detail: https://leetcode.com/submissions/detail/354910052/
# datetime: Wed Jun 17 22:17:36 2020
# runtime: 104 ms
# memory: 19.8 MB

import collections
import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        stops = [(0, src, K)]
        graph = collections.defaultdict(list)
        for s, d, c in flights:
            graph[s].append([d, c])
        while stops:
            c, s, k = heapq.heappop(stops)
            if s == dst:
                return c
            if k < 0:
                continue
            for d, c_ in graph[s]:
                heapq.heappush(stops, (c + c_, d, k - 1))
        return -1