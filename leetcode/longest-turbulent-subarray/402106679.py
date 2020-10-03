# title: longest-turbulent-subarray
# detail: https://leetcode.com/submissions/detail/402106679/
# datetime: Tue Sep 29 12:44:39 2020
# runtime: 452 ms
# memory: 18.4 MB

class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        a, b, m = 1, 1, 1
        for i in range(1, len(A)):
            if A[i] > A[i - 1]:
                a, b = 1, a + 1
            elif A[i] == A[i - 1]:
                a, b = 1, 1
            else:
                a, b = b + 1, 1
            m = max(m, a, b)
        return m