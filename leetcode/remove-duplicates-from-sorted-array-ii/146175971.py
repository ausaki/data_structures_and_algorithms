# title: remove-duplicates-from-sorted-array-ii
# detail: https://leetcode.com/submissions/detail/146175971/
# datetime: Wed Mar 21 11:24:53 2018
# runtime: 63 ms
# memory: N/A

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length == 0 or length == 1:
            return length
        prev_num = nums[0]
        count = 1
        
        i = 1
        while i < length:
            if nums[i] == prev_num:
                count += 1
                if count > 2:
                    nums.pop(i)
                    length -= 1
                else:
                    i += 1
            else:
                prev_num = nums[i]
                count = 1
                i += 1
        return length
        