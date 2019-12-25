# title: coin-change-2
# detail: https://leetcode.com/submissions/detail/286632673/
# datetime: Tue Dec 17 21:57:54 2019
# runtime: 152 ms
# memory: 51.2 MB

from functools import lru_cache
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @lru_cache(None)
        def _change(amount, i):
            if amount < 0:
                return 0
            if amount == 0:
                return 1
            if i < 0:
                return 0
            return _change(amount - coins[i], i) + _change(amount, i - 1)
        coins.sort()
        return _change(amount, len(coins) - 1)