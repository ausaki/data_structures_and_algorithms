# title: maximum-number-of-events-that-can-be-attended-ii
# detail: https://leetcode.com/submissions/detail/452801846/
# datetime: Sun Feb  7 00:48:46 2021
# runtime: 1468 ms
# memory: 59.2 MB

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
        prev = [0] * (n + 1)
        curr = [0] * (n + 1)
        for k_ in range(1, k + 1):
            for i in reversed(range(n)):
                e = events[i][1] + 1
                j = bisect.bisect(events, [e], i)
                curr[i] = max(events[i][2] + prev[j], curr[i + 1])
            prev, curr = curr, prev
        return prev[0]
        
