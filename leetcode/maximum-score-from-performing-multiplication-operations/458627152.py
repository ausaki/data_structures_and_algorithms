# title: maximum-score-from-performing-multiplication-operations
# detail: https://leetcode.com/submissions/detail/458627152/
# datetime: Sun Feb 21 11:12:51 2021
# runtime: 6420 ms
# memory: 25 MB

class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        # def dp(i, j):
        #     if 
        #     return max(multipliers[i] * nums[j] + dp(i + 1, j + 1),
        #         multipliers[i] * nums[j + m - i - 1] + dp(i + 1, j))
        
        n, m = len(nums), len(multipliers)
        dp = [0] * (n + 1)
        for i in reversed(range(m)):
            for j in range(i + 1):
                dp[j] = max(multipliers[i] * nums[j] + dp[j + 1],
                           multipliers[i] * nums[n - i + j - 1] + dp[j])
        return dp[0]