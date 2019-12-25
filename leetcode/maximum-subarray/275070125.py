# title: maximum-subarray
# detail: https://leetcode.com/submissions/detail/275070125/
# datetime: Fri Nov  1 20:48:34 2019
# runtime: 64 ms
# memory: 14.7 MB

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        sum = nums[0]
        
        for num in nums[1:]:
            s = num
            if sum > 0:
                s += sum
            if s > max_sum:
                max_sum = s
            sum = s
        return max_sum
        