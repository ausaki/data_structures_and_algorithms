# title: find-the-difference
# detail: https://leetcode.com/submissions/detail/279528182/
# datetime: Sun Nov 17 20:27:34 2019
# runtime: 32 ms
# memory: 12.8 MB

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ss = 0
        for c in s:
            ss ^= ord(c)
        for c in t:
            ss ^= ord(c)
        return chr(ss)
        