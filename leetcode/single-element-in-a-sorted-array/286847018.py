# title: single-element-in-a-sorted-array
# detail: https://leetcode.com/submissions/detail/286847018/
# datetime: Wed Dec 18 17:05:10 2019
# runtime: 68 ms
# memory: 14.8 MB

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            print(left, right)
            middle = (left + right) // 2
            if nums[middle] == nums[middle - 1]:
                if middle % 2:
                    left = middle + 1
                else:
                    right = middle - 2
            elif nums[middle] == nums[middle + 1]:
                if middle % 2:
                    right = middle - 1
                else:
                    left = middle + 2
            else:
                return nums[middle]
        return nums[left]