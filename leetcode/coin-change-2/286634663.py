# title: coin-change-2
# detail: https://leetcode.com/submissions/detail/286634663/
# datetime: Tue Dec 17 22:13:21 2019
# runtime: 268 ms
# memory: 12.9 MB

from functools import lru_cache
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for c in coins:
            for i in range(1, amount + 1):
                dp[i] += dp[i - c] if i >= c else 0
        return dp[amount]