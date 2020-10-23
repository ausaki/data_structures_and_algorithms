# title: k-th-smallest-prime-fraction
# detail: https://leetcode.com/submissions/detail/412218853/
# datetime: Fri Oct 23 18:10:54 2020
# runtime: 232 ms
# memory: 14.4 MB

from fractions import Fraction
class Solution:
    def kthSmallestPrimeFraction(self, A: List[int], K: int) -> List[int]:
        l, r, N = 0, 1, len(A)
        while True:
            m = (l + r) / 2
            border = [bisect.bisect(A, A[i] / m) for i in range(N)]
            cur = sum(N - i for i in border)
            if cur > K:
                r = m
            elif cur < K:
                l = m
            else:
                return max([(A[i], A[j]) for i, j in enumerate(border) if j < N], key=lambda x: x[0] / x[1])