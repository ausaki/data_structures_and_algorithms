# title: check-if-it-is-a-straight-line
# detail: https://leetcode.com/submissions/detail/394973457/
# datetime: Sun Sep 13 14:34:22 2020
# runtime: 56 ms
# memory: 14 MB

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]
        k = (y1 - y2) / (x1 - x2) if (x1 - x2) != 0 else math.inf
        for i in range(2, len(coordinates)):
            x1, y1 = coordinates[i - 1]
            x2, y2 = coordinates[i]
            k_ = (y1 - y2) / (x1 - x2) if (x1 - x2) != 0 else math.inf
            if k == k_ == math.inf:
                continue
            if (k == math.inf or k_ == math.inf) or not (-1e-5 <= k_ - k <= 1e-5):
                return False
        return True