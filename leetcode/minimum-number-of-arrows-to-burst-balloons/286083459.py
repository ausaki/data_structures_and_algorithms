# title: minimum-number-of-arrows-to-burst-balloons
# detail: https://leetcode.com/submissions/detail/286083459/
# datetime: Sun Dec 15 15:05:36 2019
# runtime: 460 ms
# memory: 18.2 MB

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points: return 0
        points.sort()
        res = 1
        left, right = points[0]
        for i in range(1, len(points)):
            x1, x2 = points[i]
            if x1 <= right:
                x1 = max(left, x1)
                right = min(right, x2)
            else:
                res += 1
                left, right = x1, x2
        return res