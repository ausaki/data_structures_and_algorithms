# title: number-of-subsequences-that-satisfy-the-given-sum-condition
# detail: https://leetcode.com/submissions/detail/378942662/
# datetime: Tue Aug 11 01:02:30 2020
# runtime: 2680 ms
# memory: 29 MB

import bisect
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = 10 ** 9 + 7
        n = len(nums)
        sorted_nums = sorted(zip(nums, range(len(nums))))
        result = 0
        for i, num in enumerate(nums):
            mi = num
            ma = target - mi
            if ma < mi:
                continue
            l = bisect.bisect_left(sorted_nums, (mi, 0))
            while sorted_nums[l][0] == mi and sorted_nums[l][1] < i:
                l += 1
            r = bisect.bisect_right(sorted_nums, (ma, n))
            if r <= l:
                continue
            result = (result + (1 << (r - l - 1))) % MOD
        return result
            