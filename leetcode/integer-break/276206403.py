# title: integer-break
# detail: https://leetcode.com/submissions/detail/276206403/
# datetime: Tue Nov  5 21:59:20 2019
# runtime: 40 ms
# memory: 13.5 MB

class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0 for _ in range(n + 1)]
        dp[0] = 1
        dp[1] = 1
        dp[2] = 1
        for i in range(3, n + 1):
            for j in range(1, i):
                v = j * dp[i - j] 
                if v > dp[i]:
                    dp[i] = v
                v = j * (i - j)
                if v > dp[i]:
                    dp[i] = v
        return dp[n]        