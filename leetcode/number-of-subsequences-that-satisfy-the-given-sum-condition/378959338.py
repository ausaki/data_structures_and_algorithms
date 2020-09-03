# title: number-of-subsequences-that-satisfy-the-given-sum-condition
# detail: https://leetcode.com/submissions/detail/378959338/
# datetime: Tue Aug 11 01:46:04 2020
# runtime: 2596 ms
# memory: 29.1 MB

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
            l = bisect.bisect_left(sorted_nums, (mi, i))
            r = bisect.bisect_right(sorted_nums, (ma, n))
            if r <= l:
                continue
            result = (result + (1 << (r - l - 1))) % MOD
        return result
            