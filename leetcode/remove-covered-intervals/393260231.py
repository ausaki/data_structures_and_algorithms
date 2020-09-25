# title: remove-covered-intervals
# detail: https://leetcode.com/submissions/detail/393260231/
# datetime: Wed Sep  9 20:36:52 2020
# runtime: 100 ms
# memory: 14.3 MB

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda k: (k[0], -k[1]))
        maxr = -1
        cnt = n = len(intervals)
        for a, b in intervals:
            if b <= maxr:
                cnt -= 1
            else:
                maxr = max(maxr, b)
        return cnt