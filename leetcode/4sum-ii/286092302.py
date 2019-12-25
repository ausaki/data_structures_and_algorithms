# title: 4sum-ii
# detail: https://leetcode.com/submissions/detail/286092302/
# datetime: Sun Dec 15 15:53:48 2019
# runtime: 284 ms
# memory: 33.6 MB

from functools import lru_cache
import bisect
class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        AB = collections.Counter(a+b for a in A for b in B)
        return sum(AB[-c-d] for c in C for d in D)