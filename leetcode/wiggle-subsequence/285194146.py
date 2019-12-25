# title: wiggle-subsequence
# detail: https://leetcode.com/submissions/detail/285194146/
# datetime: Wed Dec 11 14:05:00 2019
# runtime: 28 ms
# memory: 12.8 MB

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        N = len(nums)
        if N == 0:
            return 0
        i = 1
        while i < N and nums[0] == nums[i]:
            i += 1
        if i >= N:
            return 1
        if i == N - 1:
            return 2
        res = 1
        inc = nums[i] - nums[0]
        while i + 1 < N:
            while i + 1 < N:
                diff = nums[i + 1] - nums[i]
                if (diff == 0 or (diff ^ inc) >= 0):
                    i += 1
                else:
                    break
            res += 1
            inc = -1 if inc > 0 else 1
        return res