# title: two-city-scheduling
# detail: https://leetcode.com/submissions/detail/400458224/
# datetime: Fri Sep 25 14:44:42 2020
# runtime: 76 ms
# memory: 14.2 MB

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        m = n // 2
        dp = [10 ** 6] * (m + 1)
        dp[m] = 0
        for i in range(n - 1, -1, -1):
            for j in range(m + 1):
                k = i - j
                c = 10 ** 6
                if j < m:
                    c = min(c, costs[i][0] + dp[j + 1])
                if k < m:
                    c = min(c, costs[i][1] + dp[j])
                dp[j] = c
        return dp[0]
                            