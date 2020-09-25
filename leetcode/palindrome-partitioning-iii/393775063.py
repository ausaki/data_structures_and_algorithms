# title: palindrome-partitioning-iii
# detail: https://leetcode.com/submissions/detail/393775063/
# datetime: Thu Sep 10 23:11:09 2020
# runtime: 272 ms
# memory: 13.7 MB

class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        n = len(s)
        pa = [[0] * n for i in range(n)]
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                pa[i][j] = pa[i + 1][j - 1] + (s[i] != s[j])
        # for i in range(n):
        #     print(pa[i])
        dp = [n + 1] * (n + 1)
        dp[0] = 0
        for k in range(1, k + 1):
            dp2 = [n + 1] * (n + 1)
            for i in range(k - 1, n):
                for j in range(i + 1):
                    dp2[i + 1] = min(dp2[i + 1], (dp[i - j]) + pa[i - j][i])
            dp = dp2
        # print(dp)
        return dp[n]