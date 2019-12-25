# title: valid-parenthesis-string
# detail: https://leetcode.com/submissions/detail/283346986/
# datetime: Tue Dec  3 11:41:42 2019
# runtime: 28 ms
# memory: 12.9 MB

class Solution:
    def checkValidString(self, s: str) -> bool:
        cmin = cmax = 0
        for i in s:
            if i == '(':
                cmax += 1
                cmin += 1
            if i == ')':
                cmax -= 1
                cmin = max(cmin - 1, 0)
            if i == '*':
                cmax += 1
                cmin = max(cmin - 1, 0)
            if cmax < 0:
                return False
        return cmin == 0