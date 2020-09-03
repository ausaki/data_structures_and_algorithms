# title: pizza-with-3n-slices
# detail: https://leetcode.com/submissions/detail/385606757/
# datetime: Mon Aug 24 18:11:15 2020
# runtime: 268 ms
# memory: 13.9 MB

class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:
        @lru_cache(None)
        def dp(i, k):
            if k == 0 or i > j:
                return 0
            return max(dp(i + 1, j, k), slices[i] + dp(i + 2, j, k - 1))
        n = len(slices)
        k = n // 3
        dp = collections.deque([[0] * (k + 1) for i in range(2)])
        for i in range(n - 2, -1, -1):
            new_dp = [0] * (k + 1)
            for j in range(1, k + 1):
                new_dp[j] = max(dp[0][j], slices[i] + dp[1][j - 1])
            dp.pop()
            dp.appendleft(new_dp)
        a = dp[0][k]
        dp.clear()
        dp.extend([[0] * (k + 1) for i in range(2)])
        for i in range(n - 1, 0, -1):
            new_dp = [0] * (k + 1)
            for j in range(1, k + 1):
                new_dp[j] = max(dp[0][j], slices[i] + dp[1][j - 1])
            dp.pop()
            dp.appendleft(new_dp)
        b = dp[0][k]
        return max(a, b)