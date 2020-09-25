# title: decrypt-string-from-alphabet-to-integer-mapping
# detail: https://leetcode.com/submissions/detail/392213276/
# datetime: Mon Sep  7 16:10:50 2020
# runtime: 24 ms
# memory: 13.9 MB

class Solution:
    def freqAlphabets(self, s: str) -> str:
        result = []
        parts = s.split('#')
        n = len(parts)
        for i, p in enumerate(parts):
            l = len(p)
            j = l - 2
            if i == n - 1 or l == 1:
                j = l
            for k in range(j):
                result.append(chr(int(p[k]) + 96))
            if i != n - 1 and l > 1:
                result.append(chr(int(p[-2:]) + 96))
        return ''.join(result)