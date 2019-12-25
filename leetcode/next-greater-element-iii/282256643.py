# title: next-greater-element-iii
# detail: https://leetcode.com/submissions/detail/282256643/
# datetime: Thu Nov 28 18:18:27 2019
# runtime: 28 ms
# memory: 12.7 MB

import bisect
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        if n < 10:
            return -1
        digits = []
        while n:
            n, d = divmod(n, 10)
            if not digits or d >= digits[-1]:
                digits.append(d)
            else:
                i = bisect.bisect(digits, d)
                digits[i], d = d, digits[i]
                n = n * 10 + d
                for d in digits:
                    n = n * 10 + d
                return n if n <= (2 ** 31 - 1)  else -1
        return -1
                