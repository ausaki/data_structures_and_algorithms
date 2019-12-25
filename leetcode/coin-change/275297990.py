# title: coin-change
# detail: https://leetcode.com/submissions/detail/275297990/
# datetime: Sat Nov  2 21:32:29 2019
# runtime: 796 ms
# memory: 14 MB

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
        