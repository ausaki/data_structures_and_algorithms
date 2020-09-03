# title: form-largest-integer-with-digits-that-add-up-to-target
# detail: https://leetcode.com/submissions/detail/382290700/
# datetime: Tue Aug 18 01:08:25 2020
# runtime: 224 ms
# memory: 14.2 MB

class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        dp = [-1] * (target + 1)
        dp[0] = 0
        for i in range(1, target + 1):
            for j in range(9):
                if i >= cost[j] and dp[i - cost[j]] != -1:
                    dp[i] = max(dp[i], dp[i - cost[j]] + 1)
        result = ''
        if dp[target] == -1:
            return '0'
        for i in reversed(range(9)):
            while target >= cost[i] and dp[target - cost[i]] + 1 == dp[target]:
                result = result + str(i + 1)
                target -= cost[i]
        return result
        
        