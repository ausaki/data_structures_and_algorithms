# title: perfect-squares
# detail: https://leetcode.com/submissions/detail/284759397/
# datetime: Mon Dec  9 16:33:22 2019
# runtime: 148 ms
# memory: 12.7 MB

import math
from functools import lru_cache
class Solution:
    dp = [0, 1, 2, 3, 1]
    def numSquares(self, n: int) -> int:
        dp = self.dp
        for i in range(len(dp), n + 1):
            dp.append(0)
            s = math.sqrt(i)
            if int(s) == s:
                dp[i] = 1
                continue
            dp[i] = i
            for j in range(1, i):
                q = j ** 2
                if q > i // 2:
                    break
                if 1 + dp[i - q] < dp[i]:
                    dp[i] = 1 + dp[i - q]
        # print(dp)
        return dp[n]