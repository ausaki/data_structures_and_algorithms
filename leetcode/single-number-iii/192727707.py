# title: single-number-iii
# detail: https://leetcode.com/submissions/detail/192727707/
# datetime: Sat Dec  1 19:01:33 2018
# runtime: 80 ms
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
        onebit = (ab & (ab - 1)) ^ ab
        
        a, b = 0, 0
        for n in nums:
            if n & onebit:
                a ^= n
            else:
                b ^= n
        return a, b