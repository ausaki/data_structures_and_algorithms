# title: perfect-squares
# detail: https://leetcode.com/submissions/detail/284757709/
# datetime: Mon Dec  9 16:21:51 2019
# runtime: 4128 ms
# memory: 12.8 MB

import math
from functools import lru_cache
class Solution:
    def numSquares(self, n: int) -> int:
        if n <= 3:
            return n
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        dp[3] = 3
        dp[4] = 1
        
        for i in range(5, n + 1):
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