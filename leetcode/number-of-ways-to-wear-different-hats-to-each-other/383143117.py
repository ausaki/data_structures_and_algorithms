# title: number-of-ways-to-wear-different-hats-to-each-other
# detail: https://leetcode.com/submissions/detail/383143117/
# datetime: Wed Aug 19 17:13:13 2020
# runtime: 596 ms
# memory: 39.2 MB

from functools import lru_cache

class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        @lru_cache(None)
        def dp(i, choosen):
            if choosen == (1 << n) - 1:
                return 1
            if i < 0:
                return 0
            cnt = dp(i - 1, choosen)
            for p in range(n):
                if choosen & (1 << p):
                    continue
                if hats[p] & (1 << i):
                    cnt += dp(i - 1, choosen | (1 << p)) % MOD
            return cnt
        
        n = len(hats)
        hats = [reduce(lambda a, b: a | (1 << b), h, 0) for h in hats]
        cnt = dp(40, 0)
        return cnt % MOD