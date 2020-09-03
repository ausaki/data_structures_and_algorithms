# title: delete-and-earn
# detail: https://leetcode.com/submissions/detail/290166064/
# datetime: Wed Jan  1 11:08:37 2020
# runtime: 48 ms
# memory: 12.7 MB

from functools import lru_cache
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count = collections.Counter(nums)
        prev = None
        avoid = using = 0
        for k in sorted(count):
            if k - 1 != prev:
                avoid, using = max(avoid, using), k * count[k] + max(avoid, using)
            else:
                avoid, using = max(avoid, using), k * count[k] + avoid
            prev = k
        return max(avoid, using)