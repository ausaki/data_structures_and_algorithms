# title: target-sum
# detail: https://leetcode.com/submissions/detail/286341187/
# datetime: Mon Dec 16 15:57:52 2019
# runtime: 256 ms
# memory: 40.8 MB

from functools import lru_cache
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        @lru_cache(None)
        def find(i, target):
            if i >= N:
                return 1 if target == 0 else 0
            return find(i + 1, target - nums[i]) + find(i + 1, target + nums[i])
        N = len(nums)
        return find(0, S)