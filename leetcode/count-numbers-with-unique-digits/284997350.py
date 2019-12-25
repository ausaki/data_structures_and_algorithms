# title: count-numbers-with-unique-digits
# detail: https://leetcode.com/submissions/detail/284997350/
# datetime: Tue Dec 10 17:24:12 2019
# runtime: 28 ms
# memory: 12.9 MB

import math
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        res = 10
        prev = 9
        for i in range(2, n + 1):
            prev *= (10 - i + 1)
            res += prev
        return res