# title: minimum-number-of-days-to-eat-n-oranges
# detail: https://leetcode.com/submissions/detail/385252900/
# datetime: Mon Aug 24 01:20:30 2020
# runtime: 32 ms
# memory: 14.4 MB

from functools import lru_cache

@lru_cache(None)
def eat(n):
    if n <= 2:
        return n
    return 1 + min(n % 2 + eat(n // 2), n % 3 + eat(n // 3))

class Solution:
    # @lru_cache(None)
    def minDays(self, n: int) -> int:
        return eat(n)
