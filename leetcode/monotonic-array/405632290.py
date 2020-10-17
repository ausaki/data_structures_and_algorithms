# title: monotonic-array
# detail: https://leetcode.com/submissions/detail/405632290/
# datetime: Wed Oct  7 16:30:13 2020
# runtime: 460 ms
# memory: 20.2 MB

class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        d = 0
        for i in range(len(A) - 1):
            dd = A[i] - A[i + 1]
            if dd == 0:
                continue
            dd = -1 if dd < 0 else 1
            if d == 0:
                d = dd
                continue
            if d * dd == -1:
                return False
        return True