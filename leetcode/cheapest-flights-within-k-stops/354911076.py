# title: cheapest-flights-within-k-stops
# detail: https://leetcode.com/submissions/detail/354911076/
# datetime: Wed Jun 17 22:21:05 2020
# runtime: 68 ms
# memory: 14.5 MB

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        MAX_COST = 10000 * (K + 2)
        cost = MAX_COST
        stops = {src: 0}
        visited = {src: 0}
        graph = collections.defaultdict(list)
        for s, d, c in flights:
            graph[s].append([d, c])
        k = 0
        while k <= K and stops:
            new_stops = {}
            for s, c in stops.items():
                visited[s] = c
                for d, cc in graph[s]:
                    if d in visited and c + cc >= visited[d]:
                        continue
                    new_stops[d] = min(c + cc, new_stops.get(d, MAX_COST))
                    if d == dst:
                        cost = min(cost, new_stops[d])
            stops = new_stops
            k += 1
        
        return cost if cost < MAX_COST else -1