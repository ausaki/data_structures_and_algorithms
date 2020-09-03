# title: minimum-number-of-days-to-eat-n-oranges
# detail: https://leetcode.com/submissions/detail/385249231/
# datetime: Mon Aug 24 01:10:58 2020
# runtime: 80 ms
# memory: 16 MB

from functools import lru_cache

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
class Solution:
    @lru_cache(None)
    def minDays(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 0:
            return 0
        return 1 + min(n % 2 + self.minDays(n // 2), n % 3 + self.minDays(n // 3))
