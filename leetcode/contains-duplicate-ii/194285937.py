# title: contains-duplicate-ii
# detail: https://leetcode.com/submissions/detail/194285937/
# datetime: Mon Dec 10 10:22:22 2018
# runtime: 68 ms
# memory: 17.8 MB

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        nums = sorted(zip(nums, range(len(nums))))
        for i in range(len(nums) - 1):
            if nums[i][0] == nums[i + 1][0] and abs(nums[i][1] - nums[i + 1][1]) <= k:
                return True
        return False
            
        