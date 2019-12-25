# title: basic-calculator-ii
# detail: https://leetcode.com/submissions/detail/284512466/
# datetime: Sun Dec  8 15:56:56 2019
# runtime: 112 ms
# memory: 16 MB

class Solution:
    def calculate(self, s: str) -> int:
        expr = []
        n = 0
        k = False
        s += ' '
        for i in range(len(s)):
            if s[i].isdigit():
                n = n * 10 + int(s[i])
                k = True
            else:
                if k:
                    if expr and expr[-1] in ('*', '/'):
                        op = expr.pop()
                        a = expr.pop()
                        if op == '*':
                            n = a * n
                        else:
                            n = int(a / n)
                    expr.append(n)
                    k = False
                    n = 0
                if s[i] != ' ':
                    expr.append(s[i])
        a = expr[0]
        for i in range(1, len(expr), 2):
            if expr[i] == '+':
                a += expr[i + 1]
            else:
                a -= expr[i + 1]
        return a