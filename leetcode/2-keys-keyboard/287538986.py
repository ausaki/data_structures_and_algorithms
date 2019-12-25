# title: 2-keys-keyboard
# detail: https://leetcode.com/submissions/detail/287538986/
# datetime: Sat Dec 21 23:10:18 2019
# runtime: 28 ms
# memory: 12.7 MB

class Solution:
    def minSteps(self, n: int) -> int:
        res = 0
        d = 2
        while n > 1:
            while n % d == 0:
                res += d
                n //=d
            d += 1
        return res
        