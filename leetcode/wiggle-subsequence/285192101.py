# title: wiggle-subsequence
# detail: https://leetcode.com/submissions/detail/285192101/
# datetime: Wed Dec 11 13:56:27 2019
# runtime: 32 ms
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
        res = 1
        inc = nums[0] - nums[i]
        while i < N:
            while i + 1 < N:
                diff = nums[i] - nums[i + 1]
                if (diff == 0 or (diff ^ inc) >= 0):
                    i += 1
                else:
                    break
            res += 1
            inc = -1 if inc > 0 else 1
            if i + 1 >= N:
                break
        return res
        