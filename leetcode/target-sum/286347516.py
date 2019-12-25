# title: target-sum
# detail: https://leetcode.com/submissions/detail/286347516/
# datetime: Mon Dec 16 16:41:12 2019
# runtime: 2412 ms
# memory: 15.9 MB

from functools import lru_cache
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        @lru_cache(1000)
        def find(i, target):
            if target < 0:
                return 0
            if i >= N:
                return 1 if target == 0 else 0
            r = find(i + 1, target - nums[i]) + find(i + 1, target)
            return r

        N = len(nums)
        target = (sum(nums) - S) / 2
        return find(0, target)