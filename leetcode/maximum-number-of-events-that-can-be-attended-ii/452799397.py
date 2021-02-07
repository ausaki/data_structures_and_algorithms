# title: maximum-number-of-events-that-can-be-attended-ii
# detail: https://leetcode.com/submissions/detail/452799397/
# datetime: Sun Feb  7 00:41:42 2021
# runtime: 2036 ms
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
        dp = [0] * (n + 1)
        for k_ in range(1, k + 1):
            dp2 = [0] * (n + 1)
            for i in reversed(range(n)):
                e = events[i][1] + 1
                j = bisect.bisect(events, [e], i)
                dp2[i] = max(events[i][2] + dp[j], dp2[i + 1])
            dp = dp2
        return dp[0]
        
