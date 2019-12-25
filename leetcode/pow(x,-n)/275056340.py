# title: pow(x,-n)
# detail: https://leetcode.com/submissions/detail/275056340/
# datetime: Fri Nov  1 18:09:46 2019
# runtime: 40 ms
# memory: 13.9 MB

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            n = -n
            x = 1 / x
        
        p = x
        pow = 1
        while n > 1:
            if n % 2:
                pow *= p
            p *= p
            n = n // 2
        
        return pow * p
        
        