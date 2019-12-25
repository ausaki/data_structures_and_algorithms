# title: minimum-moves-to-equal-array-elements
# detail: https://leetcode.com/submissions/detail/286144601/
# datetime: Sun Dec 15 23:16:05 2019
# runtime: 260 ms
# memory: 14 MB

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        m = min(nums)
        return sum(nums) - m * len(nums)
                