# title: longest-duplicate-substring
# detail: https://leetcode.com/submissions/detail/400064708/
# datetime: Thu Sep 24 17:20:01 2020
# runtime: 3096 ms
# memory: 31.4 MB

class Solution:
    def longestDupSubstring(self, S: str) -> str:
        n = len(S)
        BASE = 26
        MOD = (1 << 63) - 1
        POWS = [1] * n
        for i in range(1, n):
            POWS[i] = (POWS[i - 1] * BASE) % MOD
        def search(k):
            seen = set()
            h = 0
            for i in range(k):
                h = (h * BASE + ord(S[i]) - 97) % MOD
            seen.add(h)
            for i in range(k, n):
                h = ((h - (ord(S[i - k]) - 97) * POWS[k - 1]) * BASE + ord(S[i]) - 97) % MOD
                s = S[i - k + 1:i + 1]
                if h in seen:
                    return i
                seen.add(h)
            return -1
        
        l, r = 0, n - 1
        while l <= r:
            m = (l + r) // 2
            if search(m) >= 0:
                l = m + 1
            else:
                r = m - 1
        if r < 0:
            return ''
        i = search(r)
        return S[i - r + 1:i + 1]