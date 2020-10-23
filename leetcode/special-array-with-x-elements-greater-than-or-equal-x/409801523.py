# title: special-array-with-x-elements-greater-than-or-equal-x
# detail: https://leetcode.com/submissions/detail/409801523/
# datetime: Sat Oct 17 20:57:15 2020
# runtime: 36 ms
# memory: 14.2 MB

class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        for i, j in enumerate(nums):
            if i and j == nums[i - 1]:
                continue
            x = len(nums) - i
            if x <= j and (i == 0 or x > nums[i - 1]):
                return x
        return -1