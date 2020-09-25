# title: minimum-remove-to-make-valid-parentheses
# detail: https://leetcode.com/submissions/detail/394541999/
# datetime: Sat Sep 12 17:07:14 2020
# runtime: 156 ms
# memory: 15.8 MB

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        idx = []
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            elif c == ')':
                if stack:
                    stack.pop()
                else:
                    idx.append(i)
        idx.extend(stack)
        result = []
        j = 0
        for i, c in enumerate(s):
            if j < len(idx) and i == idx[j]:
                j += 1
                continue
            result.append(c)
        return ''.join(result)
            
                
                    