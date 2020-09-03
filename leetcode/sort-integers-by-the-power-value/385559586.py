# title: sort-integers-by-the-power-value
# detail: https://leetcode.com/submissions/detail/385559586/
# datetime: Mon Aug 24 15:20:51 2020
# runtime: 148 ms
# memory: 23.6 MB

class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        @lru_cache(None)
        def power(x):
            if x == 1:
                return 0
            if x & 1:
                return power(3 * x + 1) + 1
            return power(x // 2) + 1
        
        return sorted(range(lo, hi + 1), key=power)[k - 1]