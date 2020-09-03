# title: minimum-number-of-days-to-eat-n-oranges
# detail: https://leetcode.com/submissions/detail/385247677/
# datetime: Mon Aug 24 01:07:05 2020
# runtime: 44 ms
# memory: 14.3 MB

from functools import lru_cache
class Solution:
    def minDays(self, n: int) -> int:
        @lru_cache(None)
        def eat(n):
            if n == 1:
                return 1
            if n == 0:
                return 0
            # if n % 3 == 0:
            #     return eat(n // 3) + 1
            # if n % 2 == 0:
            #     return eat(n // 2) + 1
            return 1 + min(n % 2 + eat(n // 2), n % 3 + eat(n // 3))
        return eat(n)
    
        # dp = [0] * (n + 1)
        # dp[1] = 1
        # for i in range(2, n + 1):
        #     dp[i] = dp[i - 1]
        #     if i % 2 == 0:
        #         dp[i] = min(dp[i], dp[i // 2])
        #     if i % 3 == 0:
        #         dp[i] = min(dp[i], dp[i // 3])
        #     dp[i] += 1
        # # print(dp)
        # return dp[n]