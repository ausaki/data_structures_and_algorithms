# title: stone-game-iv
# detail: https://leetcode.com/submissions/detail/377992377/
# datetime: Sun Aug  9 02:10:21 2020
# runtime: 192 ms
# memory: 14.7 MB

from functools import lru_cache

class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        debug = False
        dp = [0] * (n+1)
        squares = [i*i for i in range(1,int(n**0.5)+1)]
        if debug: print(f'squares = {squares}')
        # number stones -> win or lose (default lose)
        for i in range(0,n+1):
            if dp[i]:
                continue     
            for x in squares:
                if i + x > n: break
                # genius idea
                dp[i+x] = 1
        if debug: print(f'dp = {dp}')     
        return dp[-1]