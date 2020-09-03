# title: number-of-subsequences-that-satisfy-the-given-sum-condition
# detail: https://leetcode.com/submissions/detail/378961479/
# datetime: Tue Aug 11 01:51:31 2020
# runtime: 2040 ms
# memory: 25.2 MB

import bisect
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = 10 ** 9 + 7
        n = len(nums)
        nums.sort()
        result = 0
        for i, num in enumerate(nums):
            ma = target - num
            if ma < num:
                continue
            r = bisect.bisect_right(nums, ma, i, n)
            if r <= i:
                continue
            result = (result + (1 << (r - i - 1))) % MOD
        return result
            