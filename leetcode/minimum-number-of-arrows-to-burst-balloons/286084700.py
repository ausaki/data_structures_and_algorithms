# title: minimum-number-of-arrows-to-burst-balloons
# detail: https://leetcode.com/submissions/detail/286084700/
# datetime: Sun Dec 15 15:11:57 2019
# runtime: 436 ms
# memory: 17.9 MB

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points: return 0
        points.sort(key=lambda p: p[1])
        res = 1
        shot_x = points[0][1]
        for i in range(1, len(points)):
            if points[i][0] > shot_x:
                shot_x = points[i][1]
                res += 1
        return res