# title: contains-duplicate-ii
# detail: https://leetcode.com/submissions/detail/194289852/
# datetime: Mon Dec 10 10:43:12 2018
# runtime: 28 ms
# memory: 16.3 MB

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # O(n)
        # O(n)
        s = dict()
        for i, n in enumerate(nums):
            if n in s and abs(s.get(n) - i) <= k:
                return True
            s[n] = i
        return False
        