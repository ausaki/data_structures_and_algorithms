# title: minimum-add-to-make-parentheses-valid
# detail: https://leetcode.com/submissions/detail/404306719/
# datetime: Sun Oct  4 16:22:50 2020
# runtime: 20 ms
# memory: 14.2 MB

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
        return result + stack