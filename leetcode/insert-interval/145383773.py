# title: insert-interval
# detail: https://leetcode.com/submissions/detail/145383773/
# datetime: Fri Mar 16 14:05:32 2018
# runtime: 76 ms
# memory: N/A

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        s = 0
        e = 0
        result = []
        if len(intervals) == 0:
            result.append(newInterval)
            return result
        
        f = False
        for i, interval in enumerate(intervals):
            if newInterval.end < interval.start:
                result.append(newInterval)
                f = True
                break
            if newInterval.start > interval.end:
                result.append(interval)
                continue
            s = min(newInterval.start, interval.start)
            e = max(newInterval.end, interval.end)
            newInterval.start = s
            newInterval.end = e
        
        if f:
            result.extend(intervals[i:])
        else:
            result.append(newInterval)
        
        return result
                