# title: largest-triangle-area
# detail: https://leetcode.com/submissions/detail/410888547/
# datetime: Tue Oct 20 11:12:39 2020
# runtime: 128 ms
# memory: 14.2 MB

class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        return max(abs(p1[0] * p2[1] + p2[0] * p3[1] + p3[0] * p1[1] - p1[0] * p3[1] - p2[0] * p1[1] - p3[0] * p2[1]) / 2 for p1, p2, p3 in itertools.combinations(points, 3))
