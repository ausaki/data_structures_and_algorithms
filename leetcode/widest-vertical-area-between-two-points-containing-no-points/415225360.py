# title: widest-vertical-area-between-two-points-containing-no-points
# detail: https://leetcode.com/submissions/detail/415225360/
# datetime: Sat Oct 31 22:38:00 2020
# runtime: 976 ms
# memory: 54.8 MB

class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        n = len(points)
        points.sort(key=lambda k: k[0])
        return max(points[j][0] - points[i][0] for i, j in zip(range(n - 1), range(1, n)))
