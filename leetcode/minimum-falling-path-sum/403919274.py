# title: minimum-falling-path-sum
# detail: https://leetcode.com/submissions/detail/403919274/
# datetime: Sat Oct  3 22:08:48 2020
# runtime: 116 ms
# memory: 14.6 MB

class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        N = len(A)
        dp = [A[N - 1][j] for j in range(N)]
        MAX = 101
        for i in range(N - 2, -1, -1):
            p = MAX
            for j in range(N):
                p, dp[j] = dp[j], min(p, dp[j], dp[j + 1] if j + 1 < N else MAX) + A[i][j]
        return min(dp)