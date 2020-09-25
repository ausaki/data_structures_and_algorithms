# title: n-th-tribonacci-number
# detail: https://leetcode.com/submissions/detail/396960533/
# datetime: Thu Sep 17 16:24:13 2020
# runtime: 28 ms
# memory: 13.7 MB

class Solution:
    def tribonacci(self, n: int) -> int:
        a, b, c = 0, 1, 1
        while n > 2:
            a, b, c = b, c, a + b + c
            n -= 1
        return [a, b, c][n]