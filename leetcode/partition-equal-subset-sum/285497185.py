# title: partition-equal-subset-sum
# detail: https://leetcode.com/submissions/detail/285497185/
# datetime: Thu Dec 12 23:46:26 2019
# runtime: 64 ms
# memory: 13.2 MB

from functools import lru_cache
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        @lru_cache(None)
        def find(i, target):
            if target == 0:
                return True
            if i < 0:
                return False
            if target < 0:
                return False
            for j in range(i, -1, -1):
                if find(j - 1, target - nums[j]):
                    return True
            return False
        N = len(nums)
        S = sum(nums)
        if S % 2:
            return False
        nums.sort()
        return find(N - 1, S // 2)