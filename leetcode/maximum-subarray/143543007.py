# title: maximum-subarray
# detail: https://leetcode.com/submissions/detail/143543007/
# datetime: Mon Mar  5 16:28:57 2018
# runtime: 51 ms
# memory: N/A

class Solution(object):
            
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prev_sum = nums[0]
        max_sum = nums[0]
        
        for num in nums[1:]:
            s = num + (prev_sum if prev_sum > 0 else 0)
            max_sum = max(max_sum, s)
            prev_sum = s
        return max_sum