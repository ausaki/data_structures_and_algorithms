# title: check-if-array-is-sorted-and-rotated
# detail: https://leetcode.com/submissions/detail/452991778/
# datetime: Sun Feb  7 10:40:01 2021
# runtime: 56 ms
# memory: 14.1 MB

class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1: return True
        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                break
        else:
            return True
        for i in range(i + 1, n - 1):
            if nums[i] > nums[i + 1]:
                break
        else:
            return nums[-1] <= nums[0]
        return False
            