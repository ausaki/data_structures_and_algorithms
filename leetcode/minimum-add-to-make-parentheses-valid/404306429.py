# title: minimum-add-to-make-parentheses-valid
# detail: https://leetcode.com/submissions/detail/404306429/
# datetime: Sun Oct  4 16:21:57 2020
# runtime: 24 ms
# memory: 14 MB

class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        stack = 0
        result = 0
        for c in S:
            if c == '(':
                stack += 1
            else:
                if not stack:
                    result += 1
                else:
                    stack -= 1
        result += stack
        return result