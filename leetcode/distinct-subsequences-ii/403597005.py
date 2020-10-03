# title: distinct-subsequences-ii
# detail: https://leetcode.com/submissions/detail/403597005/
# datetime: Sat Oct  3 01:31:31 2020
# runtime: 60 ms
# memory: 14.1 MB

class Solution:
    def distinctSubseqII(self, S: str) -> int:
        MOD = 10 ** 9 + 7
        n = len(S)
        dp = [0] * 26
        result = 0
        for i in range(n - 1, -1, -1):
            a = ord(S[i]) - 97
            old = result
            result = (2 * old + 1 - dp[a]) % MOD
            dp[a] += result - old
        return result