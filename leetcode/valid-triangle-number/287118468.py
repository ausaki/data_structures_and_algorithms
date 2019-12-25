# title: valid-triangle-number
# detail: https://leetcode.com/submissions/detail/287118468/
# datetime: Thu Dec 19 22:33:02 2019
# runtime: 420 ms
# memory: 12.8 MB

import bisect
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        N = len(nums)
        res = 0
        for i in range(N - 2):
            if nums[i] == 0: continue
            k = i + 2
            for j in range(i + 1, N - 1):
                while k < N and nums[i] + nums[j] > nums[k]:
                    k += 1
                res += k - j - 1
        return res