# title: coin-change-2
# detail: https://leetcode.com/submissions/detail/286636409/
# datetime: Tue Dec 17 22:26:16 2019
# runtime: 144 ms
# memory: 12.8 MB

from functools import lru_cache
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for c in coins:
            for i in range(c, amount + 1):
                dp[i] += dp[i - c]
        return dp[amount]