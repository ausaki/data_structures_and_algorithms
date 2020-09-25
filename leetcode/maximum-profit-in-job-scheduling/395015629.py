# title: maximum-profit-in-job-scheduling
# detail: https://leetcode.com/submissions/detail/395015629/
# datetime: Sun Sep 13 16:44:35 2020
# runtime: 672 ms
# memory: 121.6 MB

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        start = sorted(zip(startTime, range(n)))
        @lru_cache(None)
        def dp(i):
            if i == n:
                return 0
            k = start[i][1]
            end = endTime[k]
            j = bisect.bisect(start, (end, -1), i + 1)
            return max(dp(i + 1), profit[k] + dp(j) )
        return dp(0)