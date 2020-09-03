# title: maximum-score-after-splitting-a-string
# detail: https://leetcode.com/submissions/detail/383153324/
# datetime: Wed Aug 19 17:52:44 2020
# runtime: 36 ms
# memory: 13.9 MB

class Solution:
    def maxScore(self, s: str) -> int:
        zeros = 0
        ones = s.count('1')
        result = 0
        for i in range(len(s) - 1):
            if s[i] == '0':
                zeros += 1
            else:
                ones -= 1
            result = max(result, zeros + ones)
        return result