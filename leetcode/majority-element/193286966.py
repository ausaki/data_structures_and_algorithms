# title: majority-element
# detail: https://leetcode.com/submissions/detail/193286966/
# datetime: Tue Dec  4 15:12:09 2018
# runtime: 64 ms
# memory: N/A

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        times = len(nums) / 2
        counter = dict()
        for n in nums:
            counter[n] = counter.get(n, 0) + 1
            if counter[n] > times:
                return n
        