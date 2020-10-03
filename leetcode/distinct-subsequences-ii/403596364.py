# title: distinct-subsequences-ii
# detail: https://leetcode.com/submissions/detail/403596364/
# datetime: Sat Oct  3 01:29:27 2020
# runtime: 52 ms
# memory: 14.1 MB

class Solution:
    def distinctSubseqII(self, S: str) -> int:
        MOD = 10 ** 9 + 7
        n = len(S)
        dp = collections.Counter()
        result = 0
        for i in range(n - 1, -1, -1):
            old = result
            result = (2 * old + 1 - dp[S[i]]) % MOD
            dp[S[i]] += result - old
        return result