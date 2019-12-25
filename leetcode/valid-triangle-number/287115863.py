# title: valid-triangle-number
# detail: https://leetcode.com/submissions/detail/287115863/
# datetime: Thu Dec 19 22:10:49 2019
# runtime: 716 ms
# memory: 12.5 MB

import bisect
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        N = len(nums)
        res = 0
        for i in range(N):
            k = i + 2
            for j in range(i + 1, N):
                k = bisect.bisect_left(nums, nums[i] + nums[j], max(k, j + 1), N)
                res += k - j - 1
        return res