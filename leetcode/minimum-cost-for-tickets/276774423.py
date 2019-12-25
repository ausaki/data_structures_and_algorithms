# title: minimum-cost-for-tickets
# detail: https://leetcode.com/submissions/detail/276774423/
# datetime: Thu Nov  7 19:20:22 2019
# runtime: 36 ms
# memory: 12.9 MB

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        N = len(days)
        tickets = list(zip([1, 7, 30], costs))
        MAX = costs[0] * N
        dp = [MAX] * (N + 1)
        dp[N] = 0
        for i in reversed(range(N)):
            for day, cost in tickets:
                end_day = days[i] + day - 1
                j = i + 1
                while j < N and days[j] <= end_day:
                    j += 1
                c = cost + dp[j]
                if c < dp[i]:
                    dp[i] = c
        return dp[0]
            
        