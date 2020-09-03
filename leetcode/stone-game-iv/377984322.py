# title: stone-game-iv
# detail: https://leetcode.com/submissions/detail/377984322/
# datetime: Sun Aug  9 01:49:36 2020
# runtime: 284 ms
# memory: 18.5 MB

from functools import lru_cache

class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        @lru_cache(None)
        def play(n):
            if n == 1: return True
            for i in range(int(math.sqrt(n)), 0, -1):
                j = i ** 2
                if not play(n - j):
                    # print(n , True)
                    return True
            # print(n , False)
            return False
        
        return play(n)