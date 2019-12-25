# title: majority-element
# detail: https://leetcode.com/submissions/detail/193288017/
# datetime: Tue Dec  4 15:17:19 2018
# runtime: 36 ms
# memory: N/A

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        times = len(nums)//2
        while True:
            candidate = random.choice(nums)
            if sum(1 for elem in nums if elem == candidate) > times:
                return candidate
        