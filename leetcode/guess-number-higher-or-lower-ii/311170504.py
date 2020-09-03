# title: guess-number-higher-or-lower-ii
# detail: https://leetcode.com/submissions/detail/311170504/
# datetime: Tue Mar 10 18:25:48 2020
# runtime: 132 ms
# memory: 13.8 MB

from functools import lru_cache
class Solution:
    def getMoneyAmount(self, n: int) -> int:
        MAX = n * (1 + n) // 2
        
        @lru_cache(None)
        def play(i, j):
            if i >= j:
                return 0
            return min(k + max(play(i, k - 1), play(k + 1, j)) for k in range(j - 1, i - 1, -2))
        
        return play(1, n)
            