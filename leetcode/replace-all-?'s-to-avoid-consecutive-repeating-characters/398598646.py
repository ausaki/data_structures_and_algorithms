# title: replace-all-?'s-to-avoid-consecutive-repeating-characters
# detail: https://leetcode.com/submissions/detail/398598646/
# datetime: Mon Sep 21 12:39:35 2020
# runtime: 36 ms
# memory: 13.7 MB

class Solution:
    def modifyString(self, s: str) -> str:
        s = list(s)
        n = len(s)
        for i, c in enumerate(s):
            if c == '?':
                for cc in string.ascii_lowercase:
                    if (i == 0 or cc != s[i - 1]) and (i == n - 1 or cc != s[i + 1]):
                        s[i] = cc
                        break
        return ''.join(s)