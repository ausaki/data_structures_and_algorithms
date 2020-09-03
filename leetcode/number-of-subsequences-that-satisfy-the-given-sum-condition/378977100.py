# title: number-of-subsequences-that-satisfy-the-given-sum-condition
# detail: https://leetcode.com/submissions/detail/378977100/
# datetime: Tue Aug 11 02:31:07 2020
# runtime: 644 ms
# memory: 28.7 MB

import bisect

cache = [1]
    
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = 10 ** 9 + 7
        n = len(nums)
        nums.sort()
        result = 0
        l = 0
        r = n - 1
        for i in range(len(cache), n):
            cache.append((2 * cache[-1]) % MOD)
        while l <= r:
            if nums[l] + nums[r] > target:
                r -= 1
                continue
            result = (result + cache[r - l]) % MOD
            l += 1
        return result
            