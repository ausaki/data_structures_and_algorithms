# title: target-sum
# detail: https://leetcode.com/submissions/detail/286341810/
# datetime: Mon Dec 16 16:02:10 2019
# runtime: 296 ms
# memory: 36.1 MB

from functools import lru_cache
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        @lru_cache(None)
        def find(i, target):
            if i >= N:
                return 1 if target == 0 else 0
            if target > MAX or target < -MAX:
                return 0
            return find(i + 1, target - nums[i]) + find(i + 1, target + nums[i])
        N = len(nums)
        MAX = sum(nums)
        return find(0, S)