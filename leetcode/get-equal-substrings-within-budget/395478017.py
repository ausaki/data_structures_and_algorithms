# title: get-equal-substrings-within-budget
# detail: https://leetcode.com/submissions/detail/395478017/
# datetime: Mon Sep 14 14:51:07 2020
# runtime: 128 ms
# memory: 15.5 MB

class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        diff = [abs(ord(a) - ord(b)) for a, b in zip(s, t)]
        i = 0
        t = 0
        result = 0
        for j, d in enumerate(diff):
            t += d    
            while i <= j and t > maxCost:
                t -= diff[i]
                i += 1
            if i <= j:
                result = max(result, j - i + 1)
        return result                