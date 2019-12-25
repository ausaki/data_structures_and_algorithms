# title: guess-number-higher-or-lower-ii
# detail: https://leetcode.com/submissions/detail/285173659/
# datetime: Wed Dec 11 12:33:51 2019
# runtime: 128 ms
# memory: 13.6 MB

from functools import lru_cache
class Solution:
    def getMoneyAmount(self, n: int) -> int:
        MAX = n * (1 + n) // 2
        
        @lru_cache(None)
        def play(i, j):
            if i >= j:
                return 0
            res = MAX
            for k in range(j - 1, i - 1, -2):
                m = k + max(play(i, k - 1), play(k + 1, j))
                if m < res:
                    res = m
            return res
        
        return play(1, n)
            