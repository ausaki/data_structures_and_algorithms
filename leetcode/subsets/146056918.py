# title: subsets
# detail: https://leetcode.com/submissions/detail/146056918/
# datetime: Tue Mar 20 17:11:30 2018
# runtime: 49 ms
# memory: N/A

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 1:
            return [[], [nums[0],]]
        subsets = []
        subsubsets = self.subsets(nums[1:])
        for s in subsubsets:
            subsets.append(s)
        for s in subsubsets:
            s = list(s)
            s.insert(0, nums[0])
            subsets.append(s)
        return subsets
        