# title: bus-routes
# detail: https://leetcode.com/submissions/detail/410992403/
# datetime: Tue Oct 20 16:13:45 2020
# runtime: 500 ms
# memory: 52.2 MB

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        n = len(routes)
        g = collections.defaultdict(list)
        for i, rt in enumerate(routes):
            for j in range(1, len(rt)):
                g[rt[j - 1]].append([rt[j], i])
            g[rt[-1]].append([rt[0], i])
        k = n.bit_length()
        mask = (1 << k) - 1
        initial = (S << k) + n
        q = [(0, initial)]
        dist = {}
        dist[initial] = 0
        while q:
            d, state = heapq.heappop(q)
            if d > dist[state]:
                continue
            stop, bus = state >> k, state & mask
            if stop == T:
                return d
            for stop2, bus2 in g[stop]:
                st = (stop2 << k) + bus2
                d2 = d + (bus != bus2)
                if d2 < dist.get(st, n + 1):
                    dist[st] = d2
                    heapq.heappush(q, (d2, st))
        return -1