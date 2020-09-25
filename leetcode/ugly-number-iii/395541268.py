# title: ugly-number-iii
# detail: https://leetcode.com/submissions/detail/395541268/
# datetime: Mon Sep 14 18:17:25 2020
# runtime: 32 ms
# memory: 13.8 MB

class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        ab = a * b // math.gcd(a, b)
        ac = a * c // math.gcd(a, c)
        bc = b * c // math.gcd(b, c)
        abc = a * bc // math.gcd(a, bc)
        
        lo = 1
        hi = int(2 * 1e9)
        while lo < hi:
            mid = (lo + hi) // 2
            cnt = mid // a + mid // b + mid // c - mid // ab - mid // ac - mid // bc + mid // abc
            if cnt < n:
                lo = mid + 1
            else:
                hi = mid
        return lo
            