# title: search-in-rotated-sorted-array-ii
# detail: https://leetcode.com/submissions/detail/146227770/
# datetime: Wed Mar 21 17:18:21 2018
# runtime: 40 ms
# memory: N/A

class Solution(object):
    def bisearch(self, nums, s, e, target):
        if s > e:
            return False
        m = (s + e) / 2
        if nums[m] == target:
            return True
        if nums[m] > target:
            return self.bisearch(nums, s, m - 1, target)
        return self.bisearch(nums, m + 1, e, target)
    
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        length = len(nums)
        if length == 0:
            return False
        if length == 1:
            return nums[0] == target
        
        index = -1
        
        for i in range(length - 1):
            if nums[i] == target:
                return True
            if nums[i] > nums[i + 1]:
                index = i
                break
        else:
            return nums[-1] == target
        if nums[0] <= target <= nums[index]:
            return self.bisearch(nums, 0, index, target)
        elif nums[index + 1] <= target <= nums[length - 1]:
            return self.bisearch(nums, index + 1, length - 1, target)
        return False
        
        