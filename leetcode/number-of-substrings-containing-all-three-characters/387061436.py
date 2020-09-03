# title: number-of-substrings-containing-all-three-characters
# detail: https://leetcode.com/submissions/detail/387061436/
# datetime: Thu Aug 27 17:47:28 2020
# runtime: 148 ms
# memory: 14 MB

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        pos = [-1] * 3
        result = 0
        for i, c in enumerate(s):
            pos[ord(c) - 97] = i
            result += 1 + min(pos)
        return result