# title: minimum-remove-to-make-valid-parentheses
# detail: https://leetcode.com/submissions/detail/394544013/
# datetime: Sat Sep 12 17:16:15 2020
# runtime: 108 ms
# memory: 16.6 MB

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s = list(s)
        stack = []
        idx = []
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            elif c == ')':
                if stack:
                    stack.pop()
                else:
                    s[i] = '#'
        while stack:
            s[stack.pop()] = '#'
        return ''.join(c for c in s if c != '#')
            
                
                    