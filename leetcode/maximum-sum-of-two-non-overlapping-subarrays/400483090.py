# title: maximum-sum-of-two-non-overlapping-subarrays
# detail: https://leetcode.com/submissions/detail/400483090/
# datetime: Fri Sep 25 16:01:41 2020
# runtime: 48 ms
# memory: 14.3 MB

class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        n = len(A)
        stack = [[n, 0]]
        s = 0
        stack.append([n - M, s])
        for i in range(n - 1, L - 1, -1):
            s += A[i] - (A[i + M] if i + M < n else 0)
            if i + M <= n and (not stack or s > stack[-1][1]):
                stack.append([i, s])
        s = 0
        result = 0
        s1 = 0
        maxl = 0
        for i in range(n):
            s += A[i] - (A[i - L] if i - L >= 0 else 0)
            s1 += (A[i - L] if i - L >= 0 else 0)  - (A[i - L - M] if i - L - M >= 0 else 0)
            maxl = max(maxl, s1)
            while stack and stack[-1][0] <= i:
                stack.pop()
            result = max(result, s + stack[-1][1])
            result = max(result, s + maxl)
        return result
        