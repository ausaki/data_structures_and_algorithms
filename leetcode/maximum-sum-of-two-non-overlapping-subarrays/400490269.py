# title: maximum-sum-of-two-non-overlapping-subarrays
# detail: https://leetcode.com/submissions/detail/400490269/
# datetime: Fri Sep 25 16:27:31 2020
# runtime: 48 ms
# memory: 14.2 MB

class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        n = len(A)
        for i in range(1, n):
            A[i] += A[i - 1]
        result, l, m = A[L + M - 1], A[L - 1], A[M - 1]
        for i in range(L + M, n):
            l = max(l, A[i - M] - A[i - L - M])
            m = max(m, A[i - L] - A[i - L - M])
            result = max(result, l + A[i] - A[i - M], m + A[i] - A[i - L])
        return result
        