# title: number-of-substrings-containing-all-three-characters
# detail: https://leetcode.com/submissions/detail/387061174/
# datetime: Thu Aug 27 17:46:25 2020
# runtime: 160 ms
# memory: 14.1 MB

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        pos = {'a': -1, 'b': -1, 'c': -1}
        result = 0
        for i, c in enumerate(s):
            pos[c] = i
            result += 1 + min(pos.values())
        return result