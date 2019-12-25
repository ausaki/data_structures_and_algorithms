# title: contains-duplicate
# detail: https://leetcode.com/submissions/detail/193992164/
# datetime: Sat Dec  8 18:40:23 2018
# runtime: 48 ms
# memory: 13.9 MB

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = set()
        for n in nums:
            if n in s:
                return True
            s.add(n)
        return False
        