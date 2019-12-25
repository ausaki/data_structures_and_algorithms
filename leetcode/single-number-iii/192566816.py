# title: single-number-iii
# detail: https://leetcode.com/submissions/detail/192566816/
# datetime: Fri Nov 30 16:28:39 2018
# runtime: 64 ms
# memory: N/A

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        set1 = set()
        for n in nums:
            if n in set1:
                set1.remove(n)
            else:
                set1.add(n)
        return list(set1)