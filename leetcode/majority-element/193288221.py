# title: majority-element
# detail: https://leetcode.com/submissions/detail/193288221/
# datetime: Tue Dec  4 15:18:22 2018
# runtime: 40 ms
# memory: N/A

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate
        