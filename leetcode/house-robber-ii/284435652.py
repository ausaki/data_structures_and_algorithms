# title: house-robber-ii
# detail: https://leetcode.com/submissions/detail/284435652/
# datetime: Sun Dec  8 10:12:36 2019
# runtime: 28 ms
# memory: 12.8 MB

from functools import lru_cache
class Solution:
    def rob(self, nums: List[int]) -> int:
        @lru_cache(None)
        def _rob(i, N):
            if i >= N:
                return 0
            return max(_rob(i + 1, N), nums[i] + _rob(i + 2, N))
        
        N = len(nums)
        if N == 0:
            return 0
        if N == 1:
            return nums[0]
        return max(_rob(0, N - 1), _rob(1, N))