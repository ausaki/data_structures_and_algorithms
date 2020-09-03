# title: form-largest-integer-with-digits-that-add-up-to-target
# detail: https://leetcode.com/submissions/detail/382284027/
# datetime: Tue Aug 18 00:50:50 2020
# runtime: 296 ms
# memory: 13.9 MB

class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        dp = [-1] * (target+1)
        dp[0] = 0
        for i in range(1, target+1):
            for j in range(len(cost)):
                dp[i] = max(dp[i], (dp[i-cost[j]] + 1) if i >= cost[j] and dp[i-cost[j]] > -1 else -1)
        # print(dp)
        if dp[target] < 0:
            return '0'
        ret = ''
        for i in range(len(cost), 0, -1):
            while target >= cost[i-1] and dp[target-cost[i-1]] == dp[target]-1:
                ret = ret + str(i)
                target -= cost[i-1]
        return ret