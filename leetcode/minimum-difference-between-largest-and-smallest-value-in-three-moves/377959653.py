# title: minimum-difference-between-largest-and-smallest-value-in-three-moves
# detail: https://leetcode.com/submissions/detail/377959653/
# datetime: Sun Aug  9 00:44:35 2020
# runtime: 540 ms
# memory: 23.7 MB

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 4:
            return 0
        
        nums.sort()
        
        result = 2 * (10 ** 9)
        for i in range(4):
            result = min(result, nums[n - (3 - i) - 1] - nums[i])
        return result