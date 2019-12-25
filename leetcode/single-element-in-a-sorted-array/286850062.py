# title: single-element-in-a-sorted-array
# detail: https://leetcode.com/submissions/detail/286850062/
# datetime: Wed Dec 18 17:27:44 2019
# runtime: 76 ms
# memory: 15 MB

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            middle = (left + right) // 2
            if nums[middle] == nums[middle ^ 1]:
                left = middle + 1
            else:
                right = middle
        return nums[left]