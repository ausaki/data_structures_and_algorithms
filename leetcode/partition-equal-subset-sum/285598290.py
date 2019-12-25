# title: partition-equal-subset-sum
# detail: https://leetcode.com/submissions/detail/285598290/
# datetime: Fri Dec 13 10:32:55 2019
# runtime: 40 ms
# memory: 13.4 MB

from functools import lru_cache
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        @lru_cache(None)
        def find(i, target):
            if target == 0:
                return True
            if i < 0 or target < 0:
                return False
            if find(i - 1, target - nums[i]):
                return True
            return find(i - 1, target)
        
        N = len(nums)
        S = sum(nums)
        if S % 2:
            return False
        # nums.sort()
        return find(N - 1, S // 2)