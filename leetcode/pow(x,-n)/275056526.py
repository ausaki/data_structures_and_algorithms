# title: pow(x,-n)
# detail: https://leetcode.com/submissions/detail/275056526/
# datetime: Fri Nov  1 18:11:46 2019
# runtime: 36 ms
# memory: 13.8 MB

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        neg = False
        if n < 0:
            neg = True
            n = -n
        
        p = x
        pow = 1
        while n > 1:
            if n % 2:
                pow *= p
            p *= p
            n = n // 2
        if neg:
            return 1 / (pow * p)
        return pow * p
        
        