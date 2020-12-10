# title: number-of-ways-to-form-a-target-string-given-a-dictionary
# detail: https://leetcode.com/submissions/detail/415243952/
# datetime: Sat Oct 31 23:27:26 2020
# runtime: 1764 ms
# memory: 20.4 MB

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
                if target[j] in cols[i]:
                    dp[j] = (dp[j] + cols[i][target[j]] * dp[j + 1]) % MOD
        return dp[0]