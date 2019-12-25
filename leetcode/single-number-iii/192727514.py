# title: single-number-iii
# detail: https://leetcode.com/submissions/detail/192727514/
# datetime: Sat Dec  1 18:58:05 2018
# runtime: 84 ms
# memory: N/A

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ab = 0
        for n in nums:
            ab ^= n
        onebit = 1
        for i in range(64):
            if ab & (2 << i):
                onebit = 2 << i
                break
        a, b = 0, 0
        for n in nums:
            if n & onebit:
                a ^= n
            else:
                b ^= n
        return a, b