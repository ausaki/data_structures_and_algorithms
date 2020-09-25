# title: get-equal-substrings-within-budget
# detail: https://leetcode.com/submissions/detail/395476911/
# datetime: Mon Sep 14 14:48:15 2020
# runtime: 160 ms
# memory: 15.3 MB

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
            if t <= maxCost:
                result = max(result, j - i + 1)
        return result                