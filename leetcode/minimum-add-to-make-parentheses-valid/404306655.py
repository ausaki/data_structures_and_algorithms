# title: minimum-add-to-make-parentheses-valid
# detail: https://leetcode.com/submissions/detail/404306655/
# datetime: Sun Oct  4 16:22:36 2020
# runtime: 32 ms
# memory: 14.1 MB

class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        stack = 0
        result = 0
        for c in S:
            if c == '(':
                stack += 1
            else:
                if stack:
                    stack -= 1
                else:
                    result += 1
        result += stack
        return result