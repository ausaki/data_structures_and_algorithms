# title: number-of-sets-of-k-non-overlapping-line-segments
# detail: https://leetcode.com/submissions/detail/410288303/
# datetime: Mon Oct 19 00:40:37 2020
# runtime: 512 ms
# memory: 14.3 MB

class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10 ** 9 + 7
        dp = list(range(n))
        for i in range(2, k + 1):
            dp2 = [0] * n
            curr = 0
            s = 0
            for j in range(n):
                curr += dp[j]
                dp2[j] = s
                s += curr
            dp = dp2
        return sum(dp) % MOD