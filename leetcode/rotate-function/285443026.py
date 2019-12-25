# title: rotate-function
# detail: https://leetcode.com/submissions/detail/285443026/
# datetime: Thu Dec 12 15:53:23 2019
# runtime: 96 ms
# memory: 14.7 MB

class Solution:
    def maxRotateFunction(self, A: List[int]) -> int:
        N = len(A)
        F0 = 0
        curr = 0
        for i in range(N):
            F0 += i * A[i]
            curr += A[i]
            A[i] = curr
        res = F0
        for i in range(1, N):
            Fi = F0 + A[N - i - 1] * i - (A[N - 1] - A[N - i - 1]) * (N - i)
            res = max(res, Fi)
        return res