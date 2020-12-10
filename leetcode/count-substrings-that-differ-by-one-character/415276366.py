# title: count-substrings-that-differ-by-one-character
# detail: https://leetcode.com/submissions/detail/415276366/
# datetime: Sun Nov  1 01:20:51 2020
# runtime: 52 ms
# memory: 14.1 MB

class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        S, T = len(s), len(t)
        result = 0
        for i in range(S):
            for j in range(T):
                if s[i] == t[j]:
                    continue
                l = 1
                while i - l >= 0 and j - l >= 0 and s[i - l] == t[j - l]:
                    l += 1
                r = 1
                while i + r < S and j + r < T and s[i + r] == t[j + r]:
                    r += 1
                result += l * r
        return result