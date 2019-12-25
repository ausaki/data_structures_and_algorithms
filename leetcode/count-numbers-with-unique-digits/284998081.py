# title: count-numbers-with-unique-digits
# detail: https://leetcode.com/submissions/detail/284998081/
# datetime: Tue Dec 10 17:29:41 2019
# runtime: 28 ms
# memory: 12.7 MB

import math
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        res = 10
        prev = 9
        for i in range(2, min(10, n + 1)):
            prev *= (10 - i + 1)
            res += prev
        return res