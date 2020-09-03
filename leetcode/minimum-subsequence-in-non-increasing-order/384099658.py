# title: minimum-subsequence-in-non-increasing-order
# detail: https://leetcode.com/submissions/detail/384099658/
# datetime: Fri Aug 21 15:38:32 2020
# runtime: 112 ms
# memory: 14 MB

class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        for i, j in enumerate(nums):
            nums[i] = -j
        heapq.heapify(nums)
        t = -sum(nums)
        s = 0
        result = []
        while s <= t:
            i = heapq.heappop(nums)
            s -= i
            t += i
            result.append(-i)
        return result