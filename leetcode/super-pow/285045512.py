# title: super-pow
# detail: https://leetcode.com/submissions/detail/285045512/
# datetime: Wed Dec 11 00:11:23 2019
# runtime: 136 ms
# memory: 16.3 MB

from functools import lru_cache
class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        mod = 1337
        a = a % mod
        if a <= 1:
            return a
        
        @lru_cache(None)
        def powmod(y):
            if y == 0:
                return a
            x = powmod(y - 1)
            return pow(x, 10) % mod
        powmod(1)
        
        mods = []
        for i, bb in enumerate(b[::-1]):
            if bb == 0:
                continue
            m = powmod(i)
            m = pow(m, bb) % mod
            mods.append(m)
        res = 1
        for i in range(len(mods)):
            res = (res * mods[i]) % mod
        return res
        