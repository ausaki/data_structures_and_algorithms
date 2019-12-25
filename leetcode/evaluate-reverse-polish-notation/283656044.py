# title: evaluate-reverse-polish-notation
# detail: https://leetcode.com/submissions/detail/283656044/
# datetime: Wed Dec  4 17:46:47 2019
# runtime: 68 ms
# memory: 13 MB

from operator import add, sub, mul, truediv
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {'+': add, '-': sub, '*': mul, '/': truediv}
        stack = []
        for tok in tokens:
            if tok not in operators:
                stack.append(int(tok))
            else:
                b = stack.pop()
                a = stack.pop()
                stack.append(int(operators[tok](a, b)))
        return stack.pop()
            