# title: minimum-number-of-taps-to-open-to-water-a-garden
# detail: https://leetcode.com/submissions/detail/391360213/
# datetime: Sat Sep  5 23:02:32 2020
# runtime: 1424 ms
# memory: 14 MB

class Solution:
    def minTaps(self, n, A):
        dp = [0] + [n + 2] * n
        for i, x in enumerate(A):
            for j in range(max(i - x + 1, 0), min(i + x, n) + 1):
                dp[j] = min(dp[j], dp[max(0, i - x)] + 1)
        return dp[n] if dp[n] < n + 2 else -1
