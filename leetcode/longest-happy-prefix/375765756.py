# title: longest-happy-prefix
# detail: https://leetcode.com/submissions/detail/375765756/
# datetime: Tue Aug  4 13:34:50 2020
# runtime: 252 ms
# memory: 18.9 MB

from functools import lru_cache
class Solution:
    def longestPrefix(self, s: str) -> str:
        N = len(s)
        dp = [0] * N
        for i in range(1, N):
            k = i - 1
            while k >= 0:
                j = dp[k]
                if s[i] == s[j]:
                    dp[i] = j + 1
                    break
                k = j - 1
        return s[:dp[N - 1]]