# title: basic-calculator-ii
# detail: https://leetcode.com/submissions/detail/284507231/
# datetime: Sun Dec  8 15:26:34 2019
# runtime: 120 ms
# memory: 15.9 MB

class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        n = 0
        k = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i].isdigit():
                n += int(s[i]) * (10 ** k)
                k += 1
            else:
                if k > 0:
                    stack.append(n)
                n = 0
                k = 0
                if s[i] != ' ':
                    stack.append(s[i])
        if k > 0:
            stack.append(n)
        a = stack.pop()
        while stack:
            op = stack.pop()
            b = stack.pop()
            if op in ('+', '-') and stack:
                op2 = stack.pop()
                if op2 in ('*', '/'):
                    c = stack.pop()
                    if op2 == '*':
                        b *= c
                    else:
                        b /= c
                    stack.append(int(b))
                    stack.append(op)
                    continue
                else:
                    stack.append(op2)
            if op == '+':
                a += b
            elif op == '-':
                a -= b
            elif op == '*':
                a *= b
            else:
                a = int(a / b)
        
        return a
                                    