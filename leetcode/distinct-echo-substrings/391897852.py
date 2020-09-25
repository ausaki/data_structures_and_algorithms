# title: distinct-echo-substrings
# detail: https://leetcode.com/submissions/detail/391897852/
# datetime: Mon Sep  7 00:59:56 2020
# runtime: 1856 ms
# memory: 14 MB

class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        n = len(text)
        result = 0
        seen = set()
#         for i in range(n):
        
        for i in range(n):
            l = i
            r = i + 1
            while r < n:
                if text[i:l + 1] == text[l + 1:r + 1] and text[i:l + 1] not in seen:
                    result += 1
                    seen.add(text[i:l + 1])
                l += 1
                r += 2
        return result