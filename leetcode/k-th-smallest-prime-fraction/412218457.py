# title: k-th-smallest-prime-fraction
# detail: https://leetcode.com/submissions/detail/412218457/
# datetime: Fri Oct 23 18:08:40 2020
# runtime: 4660 ms
# memory: 14.3 MB

from fractions import Fraction
class Solution:
    def kthSmallestPrimeFraction(self, A: List[int], K: int) -> List[int]:
#         class Row:
#             def __init__(self, i):
#                 self.denomenator = A[i]
            
#             def __getitem__(self, i):
                
        def count(val):
            cnt = 0
            max_frac = 0
            for i in range(n):
                j = bisect.bisect(A, val * A[i], 0, i)
                if j:
                    max_frac = max(max_frac, Fraction(A[j - 1], A[i]))
                cnt += j
            return cnt, max_frac
        
        n = len(A)
        l, r = Fraction(1, A[-1]), Fraction(1)
        step = l
        while l < r:
            m = (l + r) / 2
            cnt, frac = count(m)
            if cnt < K:
                l = m
            elif cnt > K:
                r = m
            else:
                return frac.numerator, frac.denominator
