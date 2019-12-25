# title: majority-element
# detail: https://leetcode.com/submissions/detail/193287169/
# datetime: Tue Dec  4 15:13:13 2018
# runtime: 60 ms
# memory: N/A

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)
        