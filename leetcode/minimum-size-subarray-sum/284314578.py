# title: minimum-size-subarray-sum
# detail: https://leetcode.com/submissions/detail/284314578/
# datetime: Sat Dec  7 21:08:39 2019
# runtime: 84 ms
# memory: 15.3 MB

class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        N = len(nums)
        if N == 0:
            return 0
        i = 0
        j = 0
        curr = 0
        res = N + 1
        while j < N:
            curr += nums[j]
            if curr < s:
                j += 1
                continue
            print(i, j, curr)
            while curr - nums[i] >= s:
                curr -= nums[i]
                i += 1
            if j - i + 1 < res:
                res = j - i + 1
            j += 1
        return res if res <= N else 0
