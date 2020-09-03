# title: sort-integers-by-the-power-value
# detail: https://leetcode.com/submissions/detail/385561118/
# datetime: Mon Aug 24 15:25:13 2020
# runtime: 188 ms
# memory: 24 MB

class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        @lru_cache(None)
        def power(x):
            if x == 1:
                return 0
            if x & 1:
                return power(3 * x + 1) + 1
            return power(x // 2) + 1
        
        return heapq.nsmallest(k, ((power(i), i) for i in range(lo, hi + 1)))[-1][1]