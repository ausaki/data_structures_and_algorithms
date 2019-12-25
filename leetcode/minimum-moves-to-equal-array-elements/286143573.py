# title: minimum-moves-to-equal-array-elements
# detail: https://leetcode.com/submissions/detail/286143573/
# datetime: Sun Dec 15 23:08:01 2019
# runtime: 268 ms
# memory: 13.8 MB

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        m = min(nums)
        return sum(num - m for num in nums)
                