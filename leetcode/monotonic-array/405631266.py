# title: monotonic-array
# detail: https://leetcode.com/submissions/detail/405631266/
# datetime: Wed Oct  7 16:26:30 2020
# runtime: 432 ms
# memory: 20.1 MB

class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        d = 0
        for i in range(len(A) - 1):
            dd = A[i] - A[i + 1]
            if dd == 0:
                continue
            if d == 0:
                d = dd
                continue
            if (d > 0 and dd < 0) or (d < 0 and dd > 0):
                return False
        return True