# title: minimum-difficulty-of-a-job-schedule
# detail: https://leetcode.com/submissions/detail/390943890/
# datetime: Fri Sep  4 22:38:01 2020
# runtime: 996 ms
# memory: 13.9 MB

class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        M = 1e6
        dp = [M for i in range(n + 1)]
        dp[n] = 0
        for j in range(1, d + 1):
            for i in range(n):
                m = -1
                dp[i] = M
                for k in range(i, n):
                    m = max(m, jobDifficulty[k])
                    dp[i] = min(dp[i], m + dp[k + 1])
            dp[n] = M
        return dp[0] if dp[0] < M else -1
                