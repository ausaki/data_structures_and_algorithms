# title: maximum-69-number
# detail: https://leetcode.com/submissions/detail/391325637/
# datetime: Sat Sep  5 21:44:39 2020
# runtime: 32 ms
# memory: 13.8 MB

class Solution:
    def maximum69Number (self, num: int) -> int:
        s = str(num)
        i = s.find('6')
        if i >= 0:
            return int(s[:i] + '9' + s[i + 1:])
        return num