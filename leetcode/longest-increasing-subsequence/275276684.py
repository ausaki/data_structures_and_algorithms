# title: longest-increasing-subsequence
# detail: https://leetcode.com/submissions/detail/275276684/
# datetime: Sat Nov  2 17:27:17 2019
# runtime: 768 ms
# memory: 13.9 MB

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        LIS = [0] * len(nums)
        LIS[0] = 1
        length = 1
        for i in range(1, len(nums)):
            m = 0
            for j in range(i):
                if nums[i] > nums[j] and LIS[j] > m:
                    m = LIS[j]
            LIS[i] = m + 1
            if LIS[i] > length:
                length = LIS[i]
        return length
        