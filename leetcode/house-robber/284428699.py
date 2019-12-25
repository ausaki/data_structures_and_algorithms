# title: house-robber
# detail: https://leetcode.com/submissions/detail/284428699/
# datetime: Sun Dec  8 09:34:21 2019
# runtime: 28 ms
# memory: 12.9 MB

from functools import lru_cache
class Solution:
    def rob(self, nums: List[int]) -> int:
        @lru_cache(None)
        def _rob(i):
            if i >= N:
                return 0
            return max(_rob(i + 1), nums[i] + _rob(i + 2))
        
        N = len(nums)
        return _rob(0)