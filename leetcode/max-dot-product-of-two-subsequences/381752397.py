# title: max-dot-product-of-two-subsequences
# detail: https://leetcode.com/submissions/detail/381752397/
# datetime: Sun Aug 16 23:00:44 2020
# runtime: 360 ms
# memory: 16.3 MB

class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        m = len(nums2)
        dp = [[0] * m for i in range(n)]
        dp[0][0] = nums1[0] * nums2[0]
        for j in range(1, m):
            dp[0][j] = max(dp[0][j - 1], nums1[0] * nums2[j])
        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], nums1[i] * nums2[0])
        for i in range(1, n):
            for j in range(1, m):
                prod = nums1[i] * nums2[j]
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1] + (prod if prod > 0 else 0), prod)
        # print(dp)
        return dp[n - 1][m - 1]