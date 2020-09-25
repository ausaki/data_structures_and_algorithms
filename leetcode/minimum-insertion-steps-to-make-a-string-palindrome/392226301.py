# title: minimum-insertion-steps-to-make-a-string-palindrome
# detail: https://leetcode.com/submissions/detail/392226301/
# datetime: Mon Sep  7 16:54:07 2020
# runtime: 800 ms
# memory: 170.9 MB

class Solution:
    def minInsertions(self, s: str) -> int:
        @lru_cache(None)
        def dp(i, j):
            if i >= j:
                return 0
            if s[i] == s[j]:
                return dp(i + 1, j - 1)
            return min(dp(i + 1, j), dp(i, j - 1)) + 1
        return dp(0, len(s) - 1)