# title: non-overlapping-intervals
# detail: https://leetcode.com/submissions/detail/285863917/
# datetime: Sat Dec 14 18:09:10 2019
# runtime: 72 ms
# memory: 16 MB

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        N = len(intervals)
        intervals.sort()
        left = 1 << 31
        res = 0
        for i, j in reversed(intervals):
            if j <= left:
                left = i
            else:
                res += 1
        return res
        
                