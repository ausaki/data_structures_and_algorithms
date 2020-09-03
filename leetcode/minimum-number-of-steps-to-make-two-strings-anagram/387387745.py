# title: minimum-number-of-steps-to-make-two-strings-anagram
# detail: https://leetcode.com/submissions/detail/387387745/
# datetime: Fri Aug 28 11:00:30 2020
# runtime: 108 ms
# memory: 14.4 MB

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        cnts = collections.Counter(s)
        cntt = collections.Counter(t)
        result = 0
        for c, cnt in cntt.items():
            cnt -= cnts.get(c, 0)
            if cnt > 0:
                result += cnt
        return result