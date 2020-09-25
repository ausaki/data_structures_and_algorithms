# title: minimum-time-visiting-all-points
# detail: https://leetcode.com/submissions/detail/394027023/
# datetime: Fri Sep 11 11:52:00 2020
# runtime: 60 ms
# memory: 13.9 MB

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        return sum(max(abs(p1[0] - p2[0]), abs(p1[1] - p2[1])) for p1, p2 in zip(points, points[1:]))
