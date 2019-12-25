# title: merge-intervals
# detail: https://leetcode.com/submissions/detail/143884503/
# datetime: Wed Mar  7 15:43:46 2018
# runtime: 111 ms
# memory: N/A

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals = sorted(intervals, key=lambda interval: (interval.start, interval.end))
        result = []
        if not intervals:
            return result
        current = intervals[0]
        for interval in intervals[1:]:
            if interval.start > current.end:
                result.append(current)
                current = interval
            else:
                current.start = min(current.start, interval.start)
                current.end = max(current.end, interval.end)
        result.append(current)
        return result
        