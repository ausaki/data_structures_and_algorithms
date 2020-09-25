# title: maximum-length-of-a-concatenated-string-with-unique-characters
# detail: https://leetcode.com/submissions/detail/394643392/
# datetime: Sat Sep 12 23:45:00 2020
# runtime: 116 ms
# memory: 57.9 MB

from functools import lru_cache

class Solution:
    def maxLength(self, A: List[str]) -> int:
        dp = [set()]
        for a in A:
            if len(set(a)) < len(a): continue
            a = set(a)
            for c in dp[:]:
                if a & c: continue
                dp.append(a | c)
        return max(len(a) for a in dp)