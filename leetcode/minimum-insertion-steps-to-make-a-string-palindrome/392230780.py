# title: minimum-insertion-steps-to-make-a-string-palindrome
# detail: https://leetcode.com/submissions/detail/392230780/
# datetime: Mon Sep  7 17:09:20 2020
# runtime: 544 ms
# memory: 14 MB

class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        dp = [0] * n
        for i in reversed(range(n)):
            dp2 = [0] * n 
            dp2[i] = 0
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp2[j] = dp[j - 1]
                else:
                    dp2[j] = min(dp[j], dp2[j - 1]) + 1
            dp = dp2
        return dp[n - 1]
