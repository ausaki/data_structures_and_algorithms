# title: number-of-sets-of-k-non-overlapping-line-segments
# detail: https://leetcode.com/submissions/detail/410289398/
# datetime: Mon Oct 19 00:44:20 2020
# runtime: 348 ms
# memory: 14.3 MB

class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10 ** 9 + 7
        dp = list(range(n))
        for i in range(2, k + 1):
            curr = 0
            s = 0
            for j in range(i - 1, n):
                curr += dp[j]
                dp[j] = s
                s += curr
        return sum(dp) % MOD