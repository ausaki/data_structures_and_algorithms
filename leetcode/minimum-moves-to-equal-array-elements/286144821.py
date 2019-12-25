# title: minimum-moves-to-equal-array-elements
# detail: https://leetcode.com/submissions/detail/286144821/
# datetime: Sun Dec 15 23:17:51 2019
# runtime: 300 ms
# memory: 14 MB

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        m = nums[0]
        s0 = nums[0]
        for i in range(1, len(nums)):
            s0 += nums[i]
            if nums[i] < m:
                m = nums[i]
        return s0 - m * len(nums)
                