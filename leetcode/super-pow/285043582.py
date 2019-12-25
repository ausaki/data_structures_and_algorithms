# title: super-pow
# detail: https://leetcode.com/submissions/detail/285043582/
# datetime: Tue Dec 10 23:58:20 2019
# runtime: 2580 ms
# memory: 12.7 MB

from functools import lru_cache
class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        mod = 1337
        a = a % mod
        if a <= 1:
            return a
        
        @lru_cache(None)
        def powmod(x, y):
            return pow(x, y) % mod
        
        mods = []
        for i, bb in enumerate(b[::-1]):
            if bb == 0:
                continue
            m = powmod(a, bb)
            for j in range(i):
                m = powmod(m, 10)
            mods.append(m)
        res = 1
        for i in range(len(mods)):
            res = (res * mods[i]) % mod
        return res
        