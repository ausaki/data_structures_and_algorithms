# title: find-minimum-in-rotated-sorted-array
# detail: https://leetcode.com/submissions/detail/284245036/
# datetime: Sat Dec  7 11:33:51 2019
# runtime: 40 ms
# memory: 13 MB

class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] <= nums[-1]:
            return nums[0]
        low = 0
        high = len(nums) - 1
        while low <= high:
            middle = (low + high) // 2
            if nums[middle] > nums[-1]:
                low = middle + 1
            else:
                if nums[middle] < nums[middle - 1]:
                    return nums[middle]
                high = middle - 1
        return nums[low]