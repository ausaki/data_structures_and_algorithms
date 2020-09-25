# title: palindrome-partitioning-iii
# detail: https://leetcode.com/submissions/detail/393785321/
# datetime: Thu Sep 10 23:39:36 2020
# runtime: 108 ms
# memory: 14 MB

class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        n = len(s)
        pa = [[0] * n for i in range(n)]
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                pa[i][j] = pa[i + 1][j - 1] + (s[i] != s[j])
        dp = [n] * (n + 1)
        dp[0] = 0
        for k in range(1, k + 1):
            for i in reversed(range(k - 1, n)):
                dp[i + 1] = min(dp[i - j] + pa[i - j][i] for j in range(i - k + 2))
        return dp[n]