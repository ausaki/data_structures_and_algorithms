# title: subsets-ii
# detail: https://leetcode.com/submissions/detail/146390250/
# datetime: Thu Mar 22 16:38:39 2018
# runtime: 63 ms
# memory: N/A

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        subsets = [[]]
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i - 1]:
                l = len(subsets)
            for j in range(len(subsets) - l, len(subsets)):
                subsets.append(subsets[j] + [nums[i]])
        return subsets