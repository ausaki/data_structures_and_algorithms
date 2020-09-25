# title: palindrome-partitioning-iii
# detail: https://leetcode.com/submissions/detail/393780552/
# datetime: Thu Sep 10 23:26:32 2020
# runtime: 112 ms
# memory: 13.7 MB

class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        n = len(s)
        pa = [[0] * n for i in range(n)]
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                pa[i][j] = pa[i + 1][j - 1] + (s[i] != s[j])
        dp = [n + 1] * (n + 1)
        dp[0] = 0
        for k in range(1, k + 1):
            for i in reversed(range(k - 1, n)):
                dp[i + 1] = min(dp[i - j] + pa[i - j][i] for j in range(min(i + 1, i - k + 3)))
            # for i in range(k - 1):
            #     dp[i] = n + 1
        return dp[n]