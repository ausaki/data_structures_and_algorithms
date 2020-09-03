# title: stone-game-iv
# detail: https://leetcode.com/submissions/detail/377980801/
# datetime: Sun Aug  9 01:40:27 2020
# runtime: 3316 ms
# memory: 162.1 MB

from functools import lru_cache

class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        @lru_cache(None)
        def play(n):
            if n == 1: return True
            for i in range(1, n):
                j = i ** 2
                if j > n:
                    break
                if not play(n - j):
                    # print(n , True)
                    return True
            # print(n , False)
            return False
        
        return play(n)