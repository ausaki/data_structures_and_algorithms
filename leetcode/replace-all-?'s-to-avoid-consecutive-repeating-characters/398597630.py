# title: replace-all-?'s-to-avoid-consecutive-repeating-characters
# detail: https://leetcode.com/submissions/detail/398597630/
# datetime: Mon Sep 21 12:36:40 2020
# runtime: 36 ms
# memory: 13.9 MB

class Solution:
    def modifyString(self, s: str) -> str:
        s = list(s)
        n = len(s)
        for i, c in enumerate(s):
            if c == '?':
                for cc in string.ascii_lowercase:
                    if (i == 0 or cc != s[i - 1]) and (i == n - 1 or cc != s[i + 1]):
                        s[i] = cc
        return ''.join(s)