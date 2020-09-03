# title: longest-subarray-of-1's-after-deleting-one-element
# detail: https://leetcode.com/submissions/detail/379857118/
# datetime: Wed Aug 12 20:52:28 2020
# runtime: 392 ms
# memory: 16.3 MB

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        prev_ones = 0
        ones = 0
        n = len(nums)
        result = 0
        i = 0
        while i < n:
            zeros = 0
            while i < n and nums[i] == 0:
                zeros += 1
                i += 1
            if zeros > 1:
                ones = 0
                continue
            new_ones = 0
            while i < n and nums[i] == 1:
                new_ones += 1
                i += 1
            result = max(result, ones + new_ones)
            ones = new_ones
        if result == n:
            result -= 1
        return result        