# title: maximum-sum-of-two-non-overlapping-subarrays
# detail: https://leetcode.com/submissions/detail/400479943/
# datetime: Fri Sep 25 15:51:15 2020
# runtime: 52 ms
# memory: 14.4 MB

class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        n = len(A)
        stack = []
        s = 0
        for i in range(n - 1, n - M - 1, -1):
            s += A[i]
        stack.append([n - M, s])
        for i in range(n - M - 1, L - 1, -1):
            s += A[i] - A[i + M]
            if s > stack[-1][1]:
                stack.append([i, s])
        s = 0
        for i in range(L):
            s += A[i]
        result = s + stack[-1][1]
        s1 = 0
        maxl = 0
        for i in range(L, n):
            s += A[i] - A[i - L]
            s1 += A[i - L] - (A[i - L - M] if i - L - M >= 0 else 0)
            maxl = max(maxl, s1)
            while stack and stack[-1][0] <= i:
                stack.pop()
            if stack:
                result = max(result, s + stack[-1][1])
            if i - L - M + 1 >= 0:
                result = max(result, s + maxl)
        return result
        