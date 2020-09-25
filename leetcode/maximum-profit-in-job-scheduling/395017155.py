# title: maximum-profit-in-job-scheduling
# detail: https://leetcode.com/submissions/detail/395017155/
# datetime: Sun Sep 13 16:50:01 2020
# runtime: 596 ms
# memory: 26.8 MB

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        start = sorted(zip(startTime, range(n)))
        dp = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            k = start[i][1]
            end = endTime[k]
            j = bisect.bisect(start, (end, -1), i + 1)
            dp[i] = max(dp[i + 1], profit[k] + dp[j])
        return dp[0]