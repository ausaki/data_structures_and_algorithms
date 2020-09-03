# title: cheapest-flights-within-k-stops
# detail: https://leetcode.com/submissions/detail/289692173/
# datetime: Mon Dec 30 14:37:59 2019
# runtime: 76 ms
# memory: 13.9 MB

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = collections.defaultdict(dict)
        seen = set()
        queue = [[0, src, 0]]
        for i, j, c in flights:
            graph[i][j] = c
        while queue:
            c, i, k = heapq.heappop(queue)
            seen.add(i)
            if i == dst:
                return c
            if k == K + 1:
                continue
            for j, c_ in graph[i].items():
                if j in seen:
                    continue
                heapq.heappush(queue, (c + c_, j, k + 1))    
            
        return -1