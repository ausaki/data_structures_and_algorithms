# title: rectangle-overlap
# detail: https://leetcode.com/submissions/detail/408565241/
# datetime: Wed Oct 14 15:48:05 2020
# runtime: 28 ms
# memory: 14.1 MB

class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        dx = min(rec1[2], rec2[2]) - max(rec1[0], rec2[0])
        dy = (min(rec1[3], rec2[3]) - max(rec1[1], rec2[1]))
        return dx > 0 and dy > 0