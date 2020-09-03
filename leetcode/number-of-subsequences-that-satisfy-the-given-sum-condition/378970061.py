# title: number-of-subsequences-that-satisfy-the-given-sum-condition
# detail: https://leetcode.com/submissions/detail/378970061/
# datetime: Tue Aug 11 02:13:11 2020
# runtime: 2028 ms
# memory: 25.3 MB

import bisect
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = 10 ** 9 + 7
        n = len(nums)
        nums.sort()
        result = 0
        r = -1
        for i, num in enumerate(nums):
            ma = target - num
            if ma < num:
                break
            if i == 0 or num != nums[i - 1]:
                r = bisect.bisect_right(nums, ma, i, n)
            if r <= i:
                continue
            result = (result + (1 << (r - i - 1))) % MOD
        return result
            