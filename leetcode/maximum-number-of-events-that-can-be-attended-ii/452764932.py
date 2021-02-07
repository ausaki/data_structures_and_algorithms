# title: maximum-number-of-events-that-can-be-attended-ii
# detail: https://leetcode.com/submissions/detail/452764932/
# datetime: Sat Feb  6 23:17:42 2021
# runtime: 1432 ms
# memory: 221.5 MB

class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        @lru_cache(None)
        def dp(i, j, k):
            if j == n:
                return 0
            if k == 0:
                return 0
            if i < 0 or events[j][0] > events[i][1]:
                return max(events[j][2] + dp(j, j + 1, k - 1), dp(i, j + 1, k))
            else:
                return dp(i, j + 1, k)
          
        n = len(events)
        events.sort(key=lambda e: (e[1], e[0], -e[2]))
        return dp(-1, 0, k)