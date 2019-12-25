# title: can-i-win
# detail: https://leetcode.com/submissions/detail/281803855/
# datetime: Tue Nov 26 18:32:59 2019
# runtime: 424 ms
# memory: 33.1 MB

from functools import lru_cache
class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        
        @lru_cache(None)
        def _play(player, left, pool):
            if left <= 0:
                return False
            for i in range(maxChoosableInteger - 1, -1, -1):
                if pool & (1 << i):
                    r = _play((player + 1) % 2, left - i - 1, pool & ~(1 << i))
                    if not r:
                        return True
            return False
        if desiredTotal <= 0:
            return True
        if maxChoosableInteger * (maxChoosableInteger + 1) // 2 < desiredTotal:
            return False
        pool = (1 << maxChoosableInteger) - 1
        return _play(0, desiredTotal, pool)
