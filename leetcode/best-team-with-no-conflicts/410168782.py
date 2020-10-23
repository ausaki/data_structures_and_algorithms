# title: best-team-with-no-conflicts
# detail: https://leetcode.com/submissions/detail/410168782/
# datetime: Sun Oct 18 15:54:05 2020
# runtime: 1832 ms
# memory: 14.4 MB

class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        n = len(scores)
        pairs = sorted(zip(ages, scores))
        dp = [0] * n
        result = 0
        for i in range(n):
            a, s = pairs[i]
            dp[i] = s
            for j in range(i):
                if pairs[j][1] <= s:
                    dp[i] = max(dp[i], s + dp[j])
            result = max(result, dp[i])
        return result