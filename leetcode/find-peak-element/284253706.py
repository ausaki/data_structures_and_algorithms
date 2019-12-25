# title: find-peak-element
# detail: https://leetcode.com/submissions/detail/284253706/
# datetime: Sat Dec  7 12:34:42 2019
# runtime: 48 ms
# memory: 12.8 MB

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        while low < high:
            middle = (low + high) // 2
            if nums[middle] > nums[middle + 1]:
                high = middle
            else:
                low = middle + 1
        return low
        