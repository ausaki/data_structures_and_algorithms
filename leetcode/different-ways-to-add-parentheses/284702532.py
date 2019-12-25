# title: different-ways-to-add-parentheses
# detail: https://leetcode.com/submissions/detail/284702532/
# datetime: Mon Dec  9 11:44:02 2019
# runtime: 32 ms
# memory: 12.9 MB

from functools import lru_cache
from operator import add, sub, mul
class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        expr = []
        n = 0
        for char in input:
            if char.isdigit():
                n = n * 10 + int(char)
            else:
                expr.append(n)
                n = 0
                expr.append(char)
        expr.append(n)
        operators = {'+': add, '-': sub, '*': mul}
        
        @lru_cache(None)
        def calc(left, right):
            if left == right:
                return [expr[left]]
            if left + 2 == right:
                return [operators[expr[left + 1]](expr[left], expr[right])]
            res = []
            for i in range(left, right, 2):
                part1 = calc(left, i)
                part2 = calc(i + 2, right)
                for p1 in part1:
                    for p2 in part2:
                        res.append(operators[expr[i + 1]](p1, p2))
            return res
        
        return calc(0, len(expr) - 1)
        