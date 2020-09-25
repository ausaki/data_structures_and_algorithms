# title: minimum-cost-to-connect-two-groups-of-points
# detail: https://leetcode.com/submissions/detail/399236593/
# datetime: Tue Sep 22 23:13:34 2020
# runtime: 444 ms
# memory: 14.1 MB

class Solution:
    def connectTwoGroups(self, cost: List[List[int]]) -> int:
        m, n = len(cost), len(cost[0])
        min_cols = [101] * n
        cols = [0] * n
        result = 0
        # greedy
        for i in range(m):
            k = 0
            for j in range(n):
                if cost[i][j] < cost[i][k]:
                    k = j
                min_cols[j] = min(min_cols[j], cost[i][j])
            cols[k] += 1
            result += cost[i][k]
        if cols.count(0) == 0:
            return result
        dp = [0] * (1 << n)
        for j, _ in enumerate(dp):
            c = 0
            for k in range(n):
                if j & (1 << k) == 0:
                    c += min_cols[k]
            dp[j] = c
        for i in range(m - 1, -1, -1):
            dp2 = [0] * (1 << n)
            for j, _ in enumerate(dp2):
                dp2[j] = min(cost[i][k] + dp[j | (1 << k)] for k in range(n))
            dp = dp2
        return dp[0]

