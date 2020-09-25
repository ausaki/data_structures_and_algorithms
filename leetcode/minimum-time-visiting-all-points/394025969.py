# title: minimum-time-visiting-all-points
# detail: https://leetcode.com/submissions/detail/394025969/
# datetime: Fri Sep 11 11:49:07 2020
# runtime: 56 ms
# memory: 13.8 MB

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        t = 0
        for i in range(len(points) - 1):
            x1, y1 = points[i]
            x2, y2 = points[i + 1]
            dx = abs(x1 - x2)
            dy = abs(y1 - y2)
            t += max(dx, dy)
        return t