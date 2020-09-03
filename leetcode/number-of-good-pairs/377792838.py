# title: number-of-good-pairs
# detail: https://leetcode.com/submissions/detail/377792838/
# datetime: Sat Aug  8 16:55:55 2020
# runtime: 32 ms
# memory: 13.8 MB

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        result = 0
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] == nums[j]:
                    result += 1
        return result