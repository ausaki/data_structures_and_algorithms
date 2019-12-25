# title: single-number-ii
# detail: https://leetcode.com/submissions/detail/192547376/
# datetime: Fri Nov 30 14:34:01 2018
# runtime: 60 ms
# memory: N/A

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        for n in nums:
            d[n] = d.get(n, 0) + 1
        for n in d:
            if d[n] == 1:
                return n