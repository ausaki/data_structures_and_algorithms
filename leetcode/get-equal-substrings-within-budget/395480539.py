# title: get-equal-substrings-within-budget
# detail: https://leetcode.com/submissions/detail/395480539/
# datetime: Mon Sep 14 14:57:22 2020
# runtime: 88 ms
# memory: 14.3 MB

class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        i = 0
        c = 0
        result = 0
        for j, d in enumerate(s):
            c += abs(ord(d) - ord(t[j]))  
            while i <= j and c > maxCost:
                c -= abs(ord(s[i]) - ord(t[i]))
                i += 1
            result = max(result, j - i + 1)
        return result                