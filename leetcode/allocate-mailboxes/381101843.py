# title: allocate-mailboxes
# detail: https://leetcode.com/submissions/detail/381101843/
# datetime: Sat Aug 15 14:28:54 2020
# runtime: 572 ms
# memory: 15.1 MB

class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        n = len(houses)
        houses.sort()
        if k == 1:
            p = houses[n // 2]
            return sum(abs(p - h) for h in houses)
        if k == n:
            return 0
        
        @lru_cache(None)
        def alloc(i, k):
            if k == 0 and i == n:
                return 0
            if k == 0 or i == n:
                return float('inf')
                
            dis = 0
            median = i
            result = alloc(i + 1, k -1)
            for j in range(i + 1, n):
                if (i + j) % 2 == 0:
                    diff = (houses[median + 1] - houses[median])
                    dis += diff * (median - i + 1) - diff * (j - 1 - median)
                    median += 1
                dis += houses[j] - houses[median]
                result = min(result, dis + alloc(j + 1, k -1))
            return result
        
        return alloc(0, k)
        
        
        