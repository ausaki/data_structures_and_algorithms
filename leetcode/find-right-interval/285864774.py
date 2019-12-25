# title: find-right-interval
# detail: https://leetcode.com/submissions/detail/285864774/
# datetime: Sat Dec 14 18:17:59 2019
# runtime: 312 ms
# memory: 18.1 MB

import bisect
class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        N = len(intervals)
        left = sorted([(j[0], i) for i, j in enumerate(intervals)])
        print(left)
        res = [-1] * N
        for i in range(N):
            j = bisect.bisect_left(left, (intervals[i][1], ))
            res[i] = left[j][1] if j < len(left) else -1
        return res