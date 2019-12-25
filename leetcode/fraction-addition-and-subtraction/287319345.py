# title: fraction-addition-and-subtraction
# detail: https://leetcode.com/submissions/detail/287319345/
# datetime: Fri Dec 20 18:24:58 2019
# runtime: 20 ms
# memory: 12.7 MB

import math
class Solution:
    def fractionAddition(self, expression: str) -> str:
        parts = expression.replace('-', '+-').split('+')
        fractions = []
        for part in parts:
            if part == '': continue
            a, b = part.split('/')
            fractions.append((int(a), int(b)))
        a, b = 0, 1
        for n, d in fractions:
            g = math.gcd(b, d) 
            c = b * d // g
            a = a * c // b + n * c // d
            b = c
        g = math.gcd(a, b)
        return '{}/{}'.format(a // g, b // g)