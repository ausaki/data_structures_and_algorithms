# title: make-the-string-great
# detail: https://leetcode.com/submissions/detail/378478552/
# datetime: Mon Aug 10 01:52:36 2020
# runtime: 32 ms
# memory: 13.9 MB

class Solution:
    def makeGood(self, s: str) -> str:
        result = []
        for char in s:
            if result and ((ord(result[-1]) + 32) == ord(char) or (ord(result[-1]) - 32) == ord(char)):
                result.pop()
            else:
                result.append(char)
        return ''.join(result)
                