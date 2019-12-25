# title: single-number
# detail: https://leetcode.com/submissions/detail/192543626/
# datetime: Fri Nov 30 14:15:17 2018
# runtime: 20 ms
# memory: N/A

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = 0
        for i in nums:
            n = n ^ i
        return n
        
        