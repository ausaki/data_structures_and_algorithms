# title: sort-colors
# detail: https://leetcode.com/submissions/detail/145887916/
# datetime: Mon Mar 19 17:50:12 2018
# runtime: 45 ms
# memory: N/A

class Solution(object):
    def qsort(self, nums, s, e):
        if s >= e:
            return
        # partition
        pivot = nums[s]
        h = s
        for i in range(s + 1, e + 1):
            if nums[i] <= pivot:
                h += 1
                nums[h], nums[i] = nums[i], nums[h]
        nums[h], nums[s] = nums[s], nums[h]
        self.qsort(nums, s, h - 1)
        self.qsort(nums, h + 1, e)
        
        
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        self.qsort(nums, 0, len(nums) - 1)
        