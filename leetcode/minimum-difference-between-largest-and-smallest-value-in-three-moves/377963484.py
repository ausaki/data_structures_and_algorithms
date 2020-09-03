# title: minimum-difference-between-largest-and-smallest-value-in-three-moves
# detail: https://leetcode.com/submissions/detail/377963484/
# datetime: Sun Aug  9 00:55:01 2020
# runtime: 500 ms
# memory: 23.8 MB

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 4:
            return 0
        return min([r - l for l, r in zip(heapq.nsmallest(4, nums), heapq.nlargest(4, nums)[::-1])])
