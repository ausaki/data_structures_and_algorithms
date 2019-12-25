# title: basic-calculator
# detail: https://leetcode.com/submissions/detail/283670152/
# datetime: Wed Dec  4 20:09:35 2019
# runtime: 180 ms
# memory: 46.1 MB

from operator import add, sub
class Solution:
    def calculate(self, s: str) -> int:
        operators = {'+': add, '-': sub}
        def calc(i, val):
            while i >= 0 and s[i] == ' ':
                i -= 1
            if i < 0:
                return i, val
            if s[i] == ')':
                i, val = calc(i - 1, 0)
                return calc(i - 1, val)
            elif s[i] == '(':
                return i, val
            elif s[i] in ['+', '-']:
                j, v = calc(i - 1, 0)
                return j, operators[s[i]](v, val)
            else:
                k = i
                while k >= 0 and s[k].isdigit():
                    k -= 1
                val = int(s[k + 1:i + 1])
                i = k
                return calc(k, val)
        N = len(s)
        _, res = calc(N - 1, 0)
        return res
            