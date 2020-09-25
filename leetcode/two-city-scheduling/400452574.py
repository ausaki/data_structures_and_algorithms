# title: two-city-scheduling
# detail: https://leetcode.com/submissions/detail/400452574/
# datetime: Fri Sep 25 14:28:19 2020
# runtime: 72 ms
# memory: 15.7 MB

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        @lru_cache(None)
        def dp(i, j):
            if i == n:
                return 0
            result = 10 ** 6
            k = i - j
            if j < m:
                result = min(result, costs[i][0] + dp(i + 1, j + 1))
            if k < m:
                result=  min(result, costs[i][1] + dp(i + 1, j))
            return result
        n = len(costs)
        m = n // 2
        return dp(0, 0)
                            