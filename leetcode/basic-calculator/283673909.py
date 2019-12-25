# title: basic-calculator
# detail: https://leetcode.com/submissions/detail/283673909/
# datetime: Wed Dec  4 20:46:33 2019
# runtime: 148 ms
# memory: 14.2 MB

from operator import add, sub
class Solution:
    # def calculate(self, s: str) -> int:
    #     operators = {'+': add, '-': sub}
    #     def calc(i, val):
    #         while i >= 0 and s[i] == ' ':
    #             i -= 1
    #         if i < 0:
    #             return i, val
    #         if s[i] == ')':
    #             i, val = calc(i - 1, 0)
    #             return calc(i - 1, val)
    #         elif s[i] == '(':
    #             return i, val
    #         elif s[i] in ['+', '-']:
    #             j, v = calc(i - 1, 0)
    #             return j, operators[s[i]](v, val)
    #         else:
    #             k = i
    #             while k >= 0 and s[k].isdigit():
    #                 k -= 1
    #             val = int(s[k + 1:i + 1])
    #             i = k
    #             return calc(k, val)
    #     N = len(s)
    #     _, res = calc(N - 1, 0)
    #     return res
    
    def calculate(self, s):
        def meval(stack):
            op1 = stack.pop() if stack else 0
            if op1 == ')':
                stack.append(op1)
                return 0
            while stack and stack[-1] != ')':
                op = stack.pop()
                op2 = stack.pop()
                if op == '+':
                    op1 += op2
                else:
                    op1 -= op2
            return op1
        
        stack = []
        N = len(s)
        i = N - 1
        while i >= 0:
            if s[i] == ' ':
                i -= 1
                continue
            if s[i].isdigit():
                k = i
                while k >= 0 and s[k].isdigit():
                    k -= 1
                v = int(s[k + 1: i + 1])
                stack.append(v)
                i = k
            elif s[i] == '(':
                v = meval(stack)
                stack.pop() # ')'
                stack.append(v)
                i -= 1
            else:
                stack.append(s[i])
                i -= 1
        
        return meval(stack)
                
        
        
            