# title: single-number-ii
# detail: https://leetcode.com/submissions/detail/192558829/
# datetime: Fri Nov 30 15:35:38 2018
# runtime: 56 ms
# memory: N/A

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = 0
        m = 0
        for i in nums:
            n = (n ^ i) & ~m
            m = (m ^ i) & ~n
        return n