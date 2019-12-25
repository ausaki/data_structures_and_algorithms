# title: rectangle-area
# detail: https://leetcode.com/submissions/detail/284496793/
# datetime: Sun Dec  8 14:28:54 2019
# runtime: 40 ms
# memory: 12.8 MB

class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        S = (C - A) * (D - B) + (G - E) * (H - F)
        x = min(C, G) - max(A, E)
        y = min(D, H) - max(B, F)
        if x <= 0 or y <= 0:
            return S
        return S - x * y