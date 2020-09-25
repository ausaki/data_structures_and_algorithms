# title: minimum-insertion-steps-to-make-a-string-palindrome
# detail: https://leetcode.com/submissions/detail/392231379/
# datetime: Mon Sep  7 17:11:38 2020
# runtime: 540 ms
# memory: 13.9 MB

class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        dp = [0] * n
        for i in reversed(range(n  - 1)):
            dp2 = [0] * n 
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp2[j] = dp[j - 1]
                else:
                    dp2[j] = min(dp[j], dp2[j - 1]) + 1
            dp = dp2
        return dp[n - 1]
