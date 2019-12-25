# title: valid-triangle-number
# detail: https://leetcode.com/submissions/detail/287118559/
# datetime: Thu Dec 19 22:33:47 2019
# runtime: 528 ms
# memory: 12.9 MB

import bisect
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        N = len(nums)
        res = 0
        for i in range(N):
            if nums[i] == 0: continue
            k = i + 2
            for j in range(i + 1, N):
                k = bisect.bisect_left(nums, nums[i] + nums[j], k, N)
                res += k - j - 1
        return res