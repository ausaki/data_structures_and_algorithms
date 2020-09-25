# title: reverse-substrings-between-each-pair-of-parentheses
# detail: https://leetcode.com/submissions/detail/395995160/
# datetime: Tue Sep 15 15:35:27 2020
# runtime: 56 ms
# memory: 13.7 MB

class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        result = []
        for i, c in enumerate(s):
            if c == '(':
                stack.append([])
            elif c == ')':
                if len(stack) % 2:
                    stack[-1].reverse()
                t = ''.join(stack.pop())
                if stack:
                    stack[-1].append(t)
                else:
                    result.append(t)
            else:
                if stack:
                    stack[-1].append(c)
                else:
                    result.append(c)
        return ''.join(result)