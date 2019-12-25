# title: solve-the-equation
# detail: https://leetcode.com/submissions/detail/287748437/
# datetime: Sun Dec 22 21:20:43 2019
# runtime: 28 ms
# memory: 12.7 MB

import re
class Solution:
    def solveEquation(self, equation: str) -> str:
        coef = []
        const = []
        left, right = equation.split('=')
        for c in re.findall(r'([+-]?\d*)x', left):
            if not c or c == '+':
                coef.append(1)
            elif c == '-':
                coef.append(-1)
            else:
                coef.append(int(c))
        for c in re.findall(r'([+-]?\d*)x', right):
            if not c or c == '+':
                coef.append(-1)
            elif c == '-':
                coef.append(1)
            else:
                coef.append(-int(c))
        print(coef)
        for c in re.findall(r'([+-]?\d+)(?=$|[+-])', left):
            print(c)
            const.append(-int(c))
        for c in re.findall(r'([+-]?\d+)(?=$|[+-])', right):
            const.append(int(c))
        print(const)
        coef = sum(coef)
        const = sum(const)
        if coef == 0:
            if const == 0:
                return 'Infinite solutions'
            else:
                return 'No solution'
        return 'x={}'.format(const // coef)
        