# title: check-if-binary-string-has-at-most-one-segment-of-ones
# detail: https://leetcode.com/submissions/detail/464490576/
# datetime: Sun Mar  7 10:41:21 2021
# runtime: 36 ms
# memory: 14.1 MB

class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        i = s.find('1')
        if i == -1:
            return True
        j = s.rfind('1')
        if i == j or i + 1 == j:
            return True
        k = s.find('0', i, j)
        return k == -1