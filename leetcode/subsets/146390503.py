# title: subsets
# detail: https://leetcode.com/submissions/detail/146390503/
# datetime: Thu Mar 22 16:40:56 2018
# runtime: 47 ms
# memory: N/A

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        if len(nums) == 1:
            return [[], [nums[0],]]
        subsets = [[]]
        for n in nums:
            l = len(subsets)
            for i in range(l):
                subsets.append(subsets[i] + [n])
        return subsets
        