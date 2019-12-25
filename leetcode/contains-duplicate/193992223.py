# title: contains-duplicate
# detail: https://leetcode.com/submissions/detail/193992223/
# datetime: Sat Dec  8 18:41:31 2018
# runtime: 48 ms
# memory: 14.8 MB

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums) != len(set(nums))
        