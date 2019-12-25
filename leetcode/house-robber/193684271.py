# title: house-robber
# detail: https://leetcode.com/submissions/detail/193684271/
# datetime: Thu Dec  6 18:36:44 2018
# runtime: 24 ms
# memory: 7 MB

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a, b = 0, 0
        for n in nums:
            a, b = b, max(b, n + a)        
        return b