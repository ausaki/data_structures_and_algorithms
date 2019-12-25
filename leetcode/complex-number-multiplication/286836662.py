# title: complex-number-multiplication
# detail: https://leetcode.com/submissions/detail/286836662/
# datetime: Wed Dec 18 16:00:42 2019
# runtime: 28 ms
# memory: 12.7 MB

class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        a1, b1 = a.split('+')
        a1 = int(a1)
        b1 = int(b1[:-1])
        a2, b2 = b.split('+')
        a2 = int(a2)
        b2 = int(b2[:-1])
        return '{}+{}i'.format(a1 * a2 - b1 * b2, a1 * b2 + a2 * b1)