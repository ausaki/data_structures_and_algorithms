# title: bus-routes
# detail: https://leetcode.com/submissions/detail/410990760/
# datetime: Tue Oct 20 16:07:15 2020
# runtime: 516 ms
# memory: 55 MB

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        n = len(routes)
        g = collections.defaultdict(list)
        for i, rt in enumerate(routes):
            for j in range(1, len(rt)):
                g[rt[j - 1]].append([rt[j], i])
            g[rt[-1]].append([rt[0], i])
        q = [(0, S, -1)]
        dist = {}
        dist[(S, -1)] = 0
        while q:
            d, stop, bus = heapq.heappop(q)
            if d > dist[(stop, bus)]:
                continue
            if stop == T:
                return d
            for stop2, bus2 in g[stop]:
                st = (stop2, bus2)
                d2 = d + (bus != bus2)
                if d2 < dist.get(st, n + 1):
                    dist[st] = d2
                    heapq.heappush(q, (d2, stop2, bus2))
        return -1