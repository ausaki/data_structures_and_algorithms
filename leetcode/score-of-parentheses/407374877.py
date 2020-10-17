# title: score-of-parentheses
# detail: https://leetcode.com/submissions/detail/407374877/
# datetime: Sun Oct 11 22:59:35 2020
# runtime: 24 ms
# memory: 14.2 MB

class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        stack = []
        S = '({})'.format(S)
        for c in S:
            if c == '(':
                stack.append(0)
            else:
                s = stack.pop()
                s = 1 if s == 0 else s * 2
                if not stack:
                    return s // 2
                stack[-1] += s