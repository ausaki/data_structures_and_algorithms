# title: delete-columns-to-make-sorted-iii
# detail: https://leetcode.com/submissions/detail/403015794/
# datetime: Thu Oct  1 15:03:24 2020
# runtime: 328 ms
# memory: 14.3 MB

class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        m, n = len(A), len(A[0])
        dp = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            for j in range(i + 1):
                a = 1 + dp[j]
                b = 10 ** 9
                if j == 0 or all(A[k][i] >= A[k][j - 1] for k in range(m)):
                    b = dp[i + 1]
                dp[j] = min(a, b)
        return dp[0]