# title: perfect-squares
# detail: https://leetcode.com/submissions/detail/284748194/
# datetime: Mon Dec  9 15:23:35 2019
# runtime: 6960 ms
# memory: 75.1 MB

import math
from functools import lru_cache
class Solution:
    @lru_cache(None)
    def numSquares(self, n: int) -> int:
        m = math.floor(math.sqrt(n))
        if m ** 2 == n:
            return 1
        r = 0
        k = n
        for i in range(m, 0, -1):
            r = n - i ** 2
            j = self.numSquares(r)
            if j < k:
                k = j
        return k + 1