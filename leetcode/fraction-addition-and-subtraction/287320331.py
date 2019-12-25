# title: fraction-addition-and-subtraction
# detail: https://leetcode.com/submissions/detail/287320331/
# datetime: Fri Dec 20 18:35:42 2019
# runtime: 20 ms
# memory: 12.9 MB

import re
import math
class Solution:
    def fractionAddition(self, expression: str) -> str:
        nums = map(lambda m: int(m[0]), re.finditer(r'[+-]?\d+', expression))
        a, b = 0, 1
        for n in nums:
            d = next(nums)
            g = math.gcd(b, d) 
            a, b = a * d // g + n * b // g, b * d // g
        g = math.gcd(a, b)
        return '{}/{}'.format(a // g, b // g)