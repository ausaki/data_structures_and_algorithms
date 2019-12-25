# title: majority-element
# detail: https://leetcode.com/submissions/detail/193280939/
# datetime: Tue Dec  4 14:42:34 2018
# runtime: 52 ms
# memory: N/A

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        return nums[len(nums) / 2]
        