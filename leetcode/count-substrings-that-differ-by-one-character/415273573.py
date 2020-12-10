# title: count-substrings-that-differ-by-one-character
# detail: https://leetcode.com/submissions/detail/415273573/
# datetime: Sun Nov  1 01:09:59 2020
# runtime: 76 ms
# memory: 14.2 MB

class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        S, T = len(s), len(t)
        result = 0
        for i in range(S):
            for j in range(T):
                if s[i] == t[j]:
                    continue
                l = 0
                for k in range(1, min(i, j) + 1):
                    if s[i - k] != t[j - k]:
                        break
                    l = k
                r = 0
                for k in range(1, min(S - i, T - j)):
                    if s[i + k] != t[j + k]:
                        break
                    r = k
                result += (l + 1) * (r + 1)
        return result