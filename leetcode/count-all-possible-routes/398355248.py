# title: count-all-possible-routes
# detail: https://leetcode.com/submissions/detail/398355248/
# datetime: Sun Sep 20 23:59:32 2020
# runtime: 1680 ms
# memory: 20.4 MB

class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        MOD = 10 ** 9 + 7
        start, finish = locations[start], locations[finish]
        locations.sort()
        start, finish = locations.index(start), locations.index(finish)
        n = len(locations)
        @lru_cache(None)
        def dp(i, f):
            res = 0
            if i == finish:
                res = 1
            if f == 0:
                return res
            for j in range(1, i + 1):
                ff = locations[i] - locations[i - j]
                if ff <= f:
                    res = (res + dp(i - j, f - ff)) % MOD
                else:
                    break
            for j in range(1, n - i):
                ff = locations[i + j] - locations[i]
                if ff <= f:
                    res = (res + dp(i + j, f - ff)) % MOD
                else:
                    break
            return res   
        
        return dp(start, fuel)