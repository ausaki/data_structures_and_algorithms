# title: minimum-difficulty-of-a-job-schedule
# detail: https://leetcode.com/submissions/detail/390937918/
# datetime: Fri Sep  4 22:17:32 2020
# runtime: 1168 ms
# memory: 13.9 MB

class Solution:
    # def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
    def minDifficulty(self, A, d):
        n, inf = len(A), float('inf')
        dp = [[inf] * n + [0] for i in range(d + 1)]
        for d in range(1, d + 1):
            for i in range(n - d + 1):
                maxd = 0
                for j in range(i, n - d + 1):
                    maxd = max(maxd, A[j])
                    dp[d][i] = min(dp[d][i], maxd + dp[d - 1][j + 1])
        return dp[d][0] if dp[d][0] < inf else -1
                