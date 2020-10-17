# title: rectangle-overlap
# detail: https://leetcode.com/submissions/detail/408565533/
# datetime: Wed Oct 14 15:49:09 2020
# runtime: 28 ms
# memory: 14.2 MB

class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        return min(rec1[2], rec2[2]) - max(rec1[0], rec2[0]) > 0 and min(rec1[3], rec2[3]) - max(rec1[1], rec2[1]) > 0