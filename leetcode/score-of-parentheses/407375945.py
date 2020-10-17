# title: score-of-parentheses
# detail: https://leetcode.com/submissions/detail/407375945/
# datetime: Sun Oct 11 23:03:26 2020
# runtime: 28 ms
# memory: 14.2 MB

class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        stack = [0]
        for c in S:
            if c == '(':
                stack.append(0)
            else:
                s = stack.pop()
                s = 1 if s == 0 else s * 2
                stack[-1] += s
        return stack.pop()