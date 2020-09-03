# title: sort-integers-by-the-power-value
# detail: https://leetcode.com/submissions/detail/385566086/
# datetime: Mon Aug 24 15:39:28 2020
# runtime: 88 ms
# memory: 14 MB

@lru_cache(None)
def power(x):
    if x == 1:
        return 0
    if x & 1:
        return power(3 * x + 1) + 1
    return power(x // 2) + 1

class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        return heapq.nsmallest(k, ((power(i), i) for i in range(lo, hi + 1)))[-1][1]