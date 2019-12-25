# title: single-number-iii
# detail: https://leetcode.com/submissions/detail/192727826/
# datetime: Sat Dec  1 19:03:17 2018
# runtime: 84 ms
# memory: N/A

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a = 0
        for x in nums:
            a ^= x
        a &= -a
        bit1, bit2 = 0, 0
        for x in nums:
            if x & a:
                bit1 ^= x
            else:
                bit2 ^= x
        return [bit1, bit2]