# title: rectangle-area
# detail: https://leetcode.com/submissions/detail/284495529/
# datetime: Sun Dec  8 14:21:41 2019
# runtime: 44 ms
# memory: 12.9 MB

class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        rec1 = [A, B, C, D]
        rec2 = [E, F, G, H]
        if rec1[0] > rec2[0]:
            rec1, rec2 = rec2, rec1
        S = (rec1[2] - rec1[0]) * (rec1[3] - rec1[1])
        S += (rec2[2] - rec2[0]) * (rec2[3] - rec2[1])
        x1 = rec2[0]
        x2 = min(rec1[2], rec2[2])
        y1 = min(rec1[3], rec2[3])
        y2 = max(rec1[1], rec2[1])
        x = x2 - x1
        y = y1 - y2
        print(x1, x2, y1, y2)
        if x <= 0 or y <= 0:
            return S
        return S - x * y