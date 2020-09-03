# title: cheapest-flights-within-k-stops
# detail: https://leetcode.com/submissions/detail/289676601/
# datetime: Mon Dec 30 13:29:40 2019
# runtime: 88 ms
# memory: 18.2 MB

from functools import lru_cache
class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        f = collections.defaultdict(dict)
        for a, b, p in flights:
            f[a][b] = p
        heap = [(0, src, k + 1)]
        while heap:
            p, i, k = heapq.heappop(heap)
            if i == dst:
                return p
            if k > 0:
                for j in f[i]:
                    heapq.heappush(heap, (p + f[i][j], j, k - 1))
        return -1