# title: monotonic-array
# detail: https://leetcode.com/submissions/detail/405631775/
# datetime: Wed Oct  7 16:28:23 2020
# runtime: 460 ms
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
            if math.copysign(1, d) * math.copysign(1, dd) == -1:
                return False
        return True