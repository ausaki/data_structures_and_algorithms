# title: find-peak-element
# detail: https://leetcode.com/submissions/detail/284252353/
# datetime: Sat Dec  7 12:25:39 2019
# runtime: 48 ms
# memory: 12.8 MB

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        N = len(nums)
        i = 0
        while i + 1 < N and nums[i] < nums[i + 1]:
            i += 1
        return i
        