# title: majority-element
# detail: https://leetcode.com/submissions/detail/193270809/
# datetime: Tue Dec  4 13:50:55 2018
# runtime: 40 ms
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
        for n, k in counter.iteritems():
            if k > times:
                return n
        