# title: minimum-cost-tree-from-leaf-values
# detail: https://leetcode.com/submissions/detail/276481787/
# datetime: Wed Nov  6 18:23:55 2019
# runtime: 228 ms
# memory: 12.8 MB

class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        N = len(arr)
        dp = [[0 for _ in range(N)] for _ in range(N)]
        MAX = (1 << 31) - 1 
        for i in reversed(range(N - 1)):
            for j in range(i + 1, N):
                m = MAX
                for k in range(i + 1, j + 1):
                    v = max(arr[i:k]) * max(arr[k:j + 1]) + dp[i][k - 1] + dp[k][j]
                    if v < m:
                        m = v
                dp[i][j] = m
        return dp[0][N - 1]
        