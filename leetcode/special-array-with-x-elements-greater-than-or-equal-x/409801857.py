# title: special-array-with-x-elements-greater-than-or-equal-x
# detail: https://leetcode.com/submissions/detail/409801857/
# datetime: Sat Oct 17 20:58:51 2020
# runtime: 28 ms
# memory: 14.1 MB

class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        for i, j in enumerate(nums):
            x = len(nums) - i
            if x <= j and (i == 0 or x > nums[i - 1]):
                return x
        return -1