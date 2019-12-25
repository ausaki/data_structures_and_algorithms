# title: missing-number
# detail: https://leetcode.com/submissions/detail/195734264/
# datetime: Tue Dec 18 16:52:40 2018
# runtime: 40 ms
# memory: 7.7 MB

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        n = len(nums)
        while i < n:
            k = nums[i]
            while 0 <= k < n:
                m = nums[k]
                nums[k] = -1
                k = m
            i += 1
        for i in range(n):
            if nums[i] != -1:
                return i
        return n