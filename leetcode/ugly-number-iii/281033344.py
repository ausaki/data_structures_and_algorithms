# title: ugly-number-iii
# detail: https://leetcode.com/submissions/detail/281033344/
# datetime: Sat Nov 23 17:52:02 2019
# runtime: 28 ms
# memory: 12.7 MB

class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        def gcd(x, y):
            while y > 0:
                x, y = y, x % y
            return x
        
        ab = a * b // gcd(a, b)
        ac = a * c // gcd(a, c)
        bc = b * c // gcd(b, c)
        abc = a * bc // gcd(a, bc)
        
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
            