# title: split-a-string-in-balanced-strings
# detail: https://leetcode.com/submissions/detail/395024659/
# datetime: Sun Sep 13 17:17:58 2020
# runtime: 24 ms
# memory: 13.9 MB

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        result = cnt = 0
        for c in s:
            cnt += 1 if c == 'L' else -1
            result += cnt == 0
        return result