# title: find-right-interval
# detail: https://leetcode.com/submissions/detail/285860588/
# datetime: Sat Dec 14 17:34:50 2019
# runtime: 328 ms
# memory: 18 MB

import bisect
class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        N = len(intervals)
        left = sorted([[j[0], i] for i, j in enumerate(intervals)])
        print(left)
        res = [-1] * N
        for i in range(N):
            j = bisect.bisect_left(left, [intervals[i][1], 0])
            res[i] = left[j][1] if j < len(left) else -1
        return res