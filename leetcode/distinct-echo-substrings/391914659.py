# title: distinct-echo-substrings
# detail: https://leetcode.com/submissions/detail/391914659/
# datetime: Mon Sep  7 01:45:07 2020
# runtime: 4780 ms
# memory: 14.3 MB

class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        n = len(text)
        result = 0
        seen = set()
        BASE = 27
        MOD = 10 ** 5
        hashs = [0] * (n + 1)
        pows = [1] * (n + 1)
        for i in range(n):
            hashs[i + 1] = (hashs[i] * BASE + ord(text[i]) - 96) % MOD
            pows[i + 1] = (pows[i] * BASE) % MOD
            
        h = lambda i, j: (hashs[j + 1] - (hashs[i] * pows[j - i + 1]) % MOD) % MOD
        
        for i in range(n):
            l = i
            r = i + 1
            while r < n:
                h1 = h(i, l)
                h2 = h(l + 1, r)
                s = text[i: l + 1]
                if h1 == h2 and s == text[l + 1: r + 1] and s not in seen:
                    result += 1
                    seen.add(s)
                l += 1
                r += 2
        return result