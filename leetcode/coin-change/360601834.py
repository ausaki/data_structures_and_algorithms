# title: coin-change
# detail: https://leetcode.com/submissions/detail/360601834/
# datetime: Wed Jul  1 16:30:42 2020
# runtime: 836 ms
# memory: 13.9 MB

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        MAX = amount + 1
        N = len(coins)
        if N == 0:
            return -1
        dp = [MAX] * (amount + 1)
        dp[0] = 0
        for i in range(min(coins), amount + 1):
            m = MAX
            for c in coins:
                if 0 <= i - c <= amount and dp[i - c] < m:
                    m = dp[i - c]
            if m < MAX:
                dp[i] = m + 1
        return dp[amount] if dp[amount] != MAX else -1
        