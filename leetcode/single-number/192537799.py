# title: single-number
# detail: https://leetcode.com/submissions/detail/192537799/
# datetime: Fri Nov 30 13:45:24 2018
# runtime: 32 ms
# memory: N/A

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = set()
        for n in nums:
            if n in s:
                s.remove(n)
            else:
                s.add(n)
        return s.pop()
        
        