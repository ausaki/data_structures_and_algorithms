# title: k-th-smallest-prime-fraction
# detail: https://leetcode.com/submissions/detail/412219504/
# datetime: Fri Oct 23 18:14:29 2020
# runtime: 268 ms
# memory: 14.4 MB

class Solution:
    def kthSmallestPrimeFraction(self, A: List[int], K: int) -> List[int]:
        def count(val):
            cnt = 0
            pairs = [0, 0]
            max_frac = 0
            for i in range(n):
                j = bisect.bisect(A, val * A[i], 0, i)
                if j:
                    f = A[j - 1] / A[i]
                    if f > max_frac:
                        max_frac = f
                        pairs = [A[j - 1], A[i]]
                cnt += j
            return cnt, pairs
        
        n = len(A)
        l, r = 1 / A[-1], 1
        step = l
        while l < r:
            m = (l + r) / 2
            cnt, frac = count(m)
            if cnt < K:
                l = m
            elif cnt > K:
                r = m
            else:
                return frac
