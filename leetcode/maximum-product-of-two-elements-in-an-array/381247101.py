# title: maximum-product-of-two-elements-in-an-array
# detail: https://leetcode.com/submissions/detail/381247101/
# datetime: Sat Aug 15 22:59:15 2020
# runtime: 64 ms
# memory: 13.8 MB

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        a, b = nums[0], nums[1]
        if a > b:
            a, b = b, a
        for i in range(2, len(nums)):
            if nums[i] <= a:
                continue
            if nums[i] <= b:
                a = nums[i]
            else:
                a, b = b, nums[i]
        return (a - 1) * (b - 1)