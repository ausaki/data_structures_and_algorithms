# title: largest-sum-of-averages
# detail: https://leetcode.com/submissions/detail/410977462/
# datetime: Tue Oct 20 15:18:27 2020
# runtime: 228 ms
# memory: 14.2 MB

class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        n = len(A)
        dp = [0] * n
        s = 0
        for i in range(n - 1, -1, -1):
            s += A[i]
            dp[i] = s / (n - i)
        for k in range(2, K + 1):
            for i in range(n - k + 1):
                dp[i] = -math.inf
                s = 0
                for j in range(i, n - k + 1):
                    s += A[j]
                    dp[i] = max(dp[i], s / (j - i + 1) + dp[j + 1])
        return dp[0]
            