# title: cheapest-flights-within-k-stops
# detail: https://leetcode.com/submissions/detail/289678989/
# datetime: Mon Dec 30 13:39:51 2019
# runtime: 168 ms
# memory: 14.7 MB

from functools import lru_cache
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        @lru_cache(None)
        def dfs(i, k):
            if i == dst:
                return 0
            if k == K + 1:
                return MAX
            res = MAX
            for j, c in graph[i].items():
                res = min(res, dfs(j, k + 1) + c)
            return res
            
        MAX = 10 ** 7
        graph = collections.defaultdict(dict)
        for i, j, c in flights:
            graph[i][j] = c
        res = dfs(src, 0)
        return res if res != MAX else -1