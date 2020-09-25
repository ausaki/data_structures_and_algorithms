# title: minimum-difficulty-of-a-job-schedule
# detail: https://leetcode.com/submissions/detail/390938219/
# datetime: Fri Sep  4 22:18:37 2020
# runtime: 1168 ms
# memory: 14.1 MB

class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        M = 1e6
        dp = [[M] * (d + 1) for i in range(n + 1)]
        dp[n][0] = 0
        for i in range(n - 1, -1, -1):
            for j in range(1, d + 1):
                m = -1
                for k in range(i, n):
                    m = max(m, jobDifficulty[k])
                    dp[i][j] = min(dp[i][j], m + dp[k + 1][j - 1])
        return dp[0][d] if dp[0][d] < M else -1
                