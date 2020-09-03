# title: number-of-subsequences-that-satisfy-the-given-sum-condition
# detail: https://leetcode.com/submissions/detail/378976261/
# datetime: Tue Aug 11 02:28:55 2020
# runtime: 720 ms
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
        cache = [1]
        for i in range(1, n):
            cache.append((2 * cache[-1]) % MOD)
        while l <= r:
            if nums[l] + nums[r] > target:
                r -= 1
                continue
            result = (result + cache[r - l]) % MOD
            l += 1
        return result
            