# title: maximum-number-of-events-that-can-be-attended-ii
# detail: https://leetcode.com/submissions/detail/452795874/
# datetime: Sun Feb  7 00:31:18 2021
# runtime: 1772 ms
# memory: 59.3 MB

'''
按 startDay 排序可以得到更快的 dp 算法
'''

class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        # @lru_cache(None)
        # def dp(i, k):
        #     if i == n or k == 0:
        #         return 0
        #     e = events[i][1] + 1
        #     j = bisect.bisect(events, [e], i)
        #     return max(events[i][2] + dp(j, k - 1), dp(i + 1, k))
        
        n = len(events)
        events.sort()
        dp = [[0] * (k + 1) for i in range(n + 1)]
        for i in reversed(range(n)):
            for k_ in range(1, k + 1):
                e = events[i][1] + 1
                j = bisect.bisect(events, [e], i)
                dp[i][k_] = max(events[i][2] + dp[j][k_ - 1], dp[i + 1][k_])
        return dp[0][k]
        
