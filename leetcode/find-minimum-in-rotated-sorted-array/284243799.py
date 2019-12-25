# title: find-minimum-in-rotated-sorted-array
# detail: https://leetcode.com/submissions/detail/284243799/
# datetime: Sat Dec  7 11:24:24 2019
# runtime: 52 ms
# memory: 12.9 MB

class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] <= nums[-1]:
            return nums[0]
        low = 0
        high = len(nums) - 1
        while low < high:
            middle = (low + high) // 2
            if nums[middle] > nums[-1]:
                low = middle + 1
            else:
                high = middle
        return nums[high]