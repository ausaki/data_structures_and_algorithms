# title: number-of-ways-to-wear-different-hats-to-each-other
# detail: https://leetcode.com/submissions/detail/383145705/
# datetime: Wed Aug 19 17:23:24 2020
# runtime: 688 ms
# memory: 31.3 MB

from functools import lru_cache

class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        def bitcount(a):
            cnt = 0
            while a:
                a &= a - 1
                cnt += 1
            return cnt
        
        @lru_cache(None)
        def dp(i, choosen, k):
            if k == n:
                return 1
            if i + k < n:
                return 0
            cnt = 0
            for p in range(n):
                if choosen & (1 << p):
                    continue
                if hats[p] & (1 << i):
                    cnt += dp(i - 1, choosen | (1 << p), k + 1) % MOD
            return cnt + dp(i - 1, choosen, k)
        
        n = len(hats)
        people_mask = (1 << n) - 1
        hats = [reduce(lambda a, b: a | (1 << b), h, 0) for h in hats]
        cnt = dp(40, 0, 0)
        return cnt % MOD