# title: maximum-width-ramp
# detail: https://leetcode.com/submissions/detail/402621265/
# datetime: Wed Sep 30 16:51:07 2020
# runtime: 312 ms
# memory: 21.1 MB

class Solution:
    def maxWidthRamp(self, A: List[int]) -> int:
        n = len(A)
        idx = sorted(range(n), key=A.__getitem__)
        i = n
        result = 0
        for j in idx:
            result = max(result, j - i)
            i = min(i, j)
        return result