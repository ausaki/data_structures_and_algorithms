# title: broken-calculator
# detail: https://leetcode.com/submissions/detail/401761885/
# datetime: Mon Sep 28 17:51:00 2020
# runtime: 28 ms
# memory: 13.9 MB

class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        result = 0
        while Y > X:
            if Y % 2:
                Y += 1
            else:
                Y //= 2
            result += 1
        return result + X - Y
        
            