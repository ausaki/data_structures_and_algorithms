# title: largest-substring-between-two-equal-characters
# detail: https://leetcode.com/submissions/detail/410074300/
# datetime: Sun Oct 18 11:24:28 2020
# runtime: 28 ms
# memory: 14.2 MB

class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        pos = {}
        result = -1
        for i, c in enumerate(s):
            if c not in pos:
                pos[c] = i
            else:
                result = max(result, i - pos[c] - 1)
        return result