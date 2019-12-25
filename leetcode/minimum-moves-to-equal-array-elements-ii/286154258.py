# title: minimum-moves-to-equal-array-elements-ii
# detail: https://leetcode.com/submissions/detail/286154258/
# datetime: Mon Dec 16 00:27:34 2019
# runtime: 84 ms
# memory: 14.1 MB

import heapq
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        middle = heapq.nsmallest(len(nums) // 2 + 1, nums)[-1]
        return sum(abs(num - middle) for num in nums)
