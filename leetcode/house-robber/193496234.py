# title: house-robber
# detail: https://leetcode.com/submissions/detail/193496234/
# datetime: Wed Dec  5 17:47:47 2018
# runtime: 24 ms
# memory: 7 MB

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.cache = [None] * len(nums)
        r = self._rob(nums, 0)
        return r

    def _rob(self, nums, s=0):
        l = len(nums) - s
        if l <= 0:
            return 0
        if l == 1:
            return nums[s]
        if self.cache[s] is not None:
            return self.cache[s]
        result1 = nums[s] + self._rob(nums, s + 2)
        result2 = nums[s + 1] + self._rob(nums, s + 3)
        result = max(result1, result2)
        self.cache[s] = result
        return result
        