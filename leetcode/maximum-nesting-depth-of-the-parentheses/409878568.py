# title: maximum-nesting-depth-of-the-parentheses
# detail: https://leetcode.com/submissions/detail/409878568/
# datetime: Sun Oct 18 00:44:15 2020
# runtime: 48 ms
# memory: 14 MB

class Solution:
    def maxDepth(self, s: str) -> int:
        stack = [0]
        for c in s:
            if c == '(':
                stack.append(0)
            elif c == ')':
                d = stack.pop()
                stack[-1] = max(stack[-1], d + 1)
        return stack[0]