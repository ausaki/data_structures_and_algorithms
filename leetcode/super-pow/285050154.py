# title: super-pow
# detail: https://leetcode.com/submissions/detail/285050154/
# datetime: Wed Dec 11 00:42:36 2019
# runtime: 148 ms
# memory: 12.6 MB

from functools import lru_cache
class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        mod = 1337
        a = a % mod
        if a <= 1:
            return a
        res = 1
        for bb in b[::-1]:
            res = (res * pow(a, bb, mod)) % mod
            a = pow(a, 10, mod)
        return res
        
        