# title: super-pow
# detail: https://leetcode.com/submissions/detail/285047268/
# datetime: Wed Dec 11 00:23:23 2019
# runtime: 224 ms
# memory: 15.5 MB

from functools import lru_cache
class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        mod = 1337
        a = a % mod
        if a <= 1:
            return a
        
        def mypow(x, y):
            d, m = divmod(y, 2)
            res = 1
            for i in range(d):
                res = (res * pow(x, 2)) % mod
            return (res * (x if m else 1)) % mod
        
        @lru_cache(None)
        def powmod(y):
            if y == 0:
                return a
            x = powmod(y - 1)
            return mypow(x, 10)
        powmod(1)
        
        mods = []
        for i, bb in enumerate(b[::-1]):
            if bb == 0:
                continue
            m = powmod(i)
            m = mypow(m, bb)
            mods.append(m)
        res = 1
        for i in range(len(mods)):
            res = (res * mods[i]) % mod
        return res
        