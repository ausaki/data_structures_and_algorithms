# title: majority-element
# detail: https://leetcode.com/submissions/detail/193286519/
# datetime: Tue Dec  4 15:10:00 2018
# runtime: 28 ms
# memory: N/A

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp=[]
        for item in nums:
            if item not in temp:
                temp.append(item)
                c = nums.count(item)
                if c>=len(nums)/2.:
                    return item
                    break
        