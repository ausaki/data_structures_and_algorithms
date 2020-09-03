# title: number-of-subsequences-that-satisfy-the-given-sum-condition
# detail: https://leetcode.com/submissions/detail/378972134/
# datetime: Tue Aug 11 02:18:21 2020
# runtime: 1984 ms
# memory: 25.1 MB

import bisect
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = 10 ** 9 + 7
        n = len(nums)
        nums.sort()
        result = 0
        l = 0
        r = n - 1
        while l <= r:
            if nums[l] + nums[r] > target:
                r -= 1
                continue
            result = (result + (1 << (r - l))) % MOD
            l += 1
        return result
            