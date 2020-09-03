# title: paint-house-iii
# detail: https://leetcode.com/submissions/detail/381236499/
# datetime: Sat Aug 15 22:28:24 2020
# runtime: 492 ms
# memory: 19.8 MB

from functools import lru_cache
import math

class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        MAX_COST = 10 ** 7
        
        @lru_cache(None)
        def paint(i, color, k):
            # print(i, k, color)
            if k == 0 and i == m:
                return 0
            if k < 0 or i == m:
                return MAX_COST
            if m - i < k:
                return MAX_COST
            if houses[i] != 0:
                return paint(i + 1, houses[i], k - (1 if houses[i] != color else 0))
            return min((cost[i][c - 1] + paint(i + 1, c, k - (1 if c != color else 0)) for c in range(1, n + 1)))
            # print(i, k, color, total_cost)
            # return total_cost
        
        # neighbors = 0
        # prev = 0
        # for h in houses:
        #     if h == 0: 
        #         continue
        #     if h != prev:
        #         neighbors += 1
        #         prev = h
        # if neighbors > target:
        #     return -1
        res = paint(0, -1, target)
        return res if res < MAX_COST else -1