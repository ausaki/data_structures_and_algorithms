# title: number-of-substrings-containing-all-three-characters
# detail: https://leetcode.com/submissions/detail/387059946/
# datetime: Thu Aug 27 17:41:38 2020
# runtime: 364 ms
# memory: 14 MB

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        pos = {'a': -1, 'b': -1, 'c': -1}
        result = 0
        for i, c in enumerate(s):
            result += 1 + min(v for k, v in pos.items() if k != c)
            pos[c] = i
        return result