# title: coin-change-2
# detail: https://leetcode.com/submissions/detail/286636364/
# datetime: Tue Dec 17 22:25:59 2019
# runtime: 136 ms
# memory: 12.7 MB

from functools import lru_cache
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for c in coins:
            for i in range(c, amount + 1):
                dp[i] += dp[i - c]
        return dp[amount]