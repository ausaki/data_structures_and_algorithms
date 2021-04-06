# title: maximum-ascending-subarray-sum
# detail: https://leetcode.com/submissions/detail/470384256/
# datetime: Sun Mar 21 10:34:31 2021
# runtime: 40 ms
# memory: 14.1 MB

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        res = nums[0]
        s = 0
        prev = -1
        for i, a in enumerate(nums):
            if a > prev:
                s += a
            else:
                s = a
            prev = a
            res = max(res, s)
        return res