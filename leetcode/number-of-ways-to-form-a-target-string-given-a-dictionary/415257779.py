# title: number-of-ways-to-form-a-target-string-given-a-dictionary
# detail: https://leetcode.com/submissions/detail/415257779/
# datetime: Sun Nov  1 00:10:50 2020
# runtime: 1456 ms
# memory: 20.5 MB

class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        MOD = 10 ** 9 + 7
        m, n, t = len(words), len(words[0]), len(target)
        if t > n:
            return 0
        cols = [collections.Counter() for i in range(n)]
        for i in range(m):
            for j in range(n):
                cols[j][words[i][j]] += 1
        
        dp = [0] * (t + 1)
        dp[-1] = 1
        for i in range(n - 1, -1, -1):
            for j in range(min(t, i + 1)):
                dp[j] = (dp[j] + cols[i][target[j]] * dp[j + 1]) % MOD
        return dp[0]