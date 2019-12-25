# title: single-number-ii
# detail: https://leetcode.com/submissions/detail/192563413/
# datetime: Fri Nov 30 16:04:19 2018
# runtime: 40 ms
# memory: N/A

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        set1 = set()
        set2 = set()
        for n in nums:
            if n in set1:
                if n in set2:
                    set1.remove(n)
                else:
                    set2.add(n)
            else:
                set1.add(n)
        return set1.pop()