# title: minimum-insertions-to-balance-a-parentheses-string
# detail: https://leetcode.com/submissions/detail/379409307/
# datetime: Tue Aug 11 23:34:00 2020
# runtime: 176 ms
# memory: 14.6 MB

class Solution:
    def minInsertions(self, s: str) -> int:
        stack = 0
        result = 0
        i = 0
        n = len(s)
        while i < n:
            if s[i] == '(':
                stack += 1
                i += 1
                continue
            if i + 1 < n and s[i + 1] == ')':
                if stack:
                    stack -= 1
                else:
                    result += 1
                i += 2
            else:
                if stack:
                    stack -= 1
                else:
                    result += 1
                result += 1
                i += 1
        if stack:
            result += stack * 2
        return result