# title: rotate-function
# detail: https://leetcode.com/submissions/detail/285448510/
# datetime: Thu Dec 12 16:26:39 2019
# runtime: 88 ms
# memory: 14.3 MB

class Solution:
    def maxRotateFunction(self, A: List[int]) -> int:
        N = len(A)
        F0 = 0
        Sum = 0
        for i in range(N):
            F0 += i * A[i]
            Sum += A[i]
        res = F0
        F = F0
        for i in range(1, N):
            F += Sum - A[N - i] * N
            res = max(res, F)
        return res