# title: ways-to-make-a-fair-array
# detail: https://leetcode.com/submissions/detail/422804006/
# datetime: Sun Nov 22 11:04:45 2020
# runtime: 1156 ms
# memory: 20.9 MB

class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        n = len(nums)
        odd, even = sum(nums[i] for i in range(1, n, 2)), sum(nums[i] for i in range(0, n, 2))
        odd1, even1 = 0, 0
        ans = 0
        for i in range(n):
            if i % 2:
                odd -= nums[i]
                if odd1 + even == even1 + odd:
                    ans += 1
                odd1 += nums[i]
            else:
                even -= nums[i]
                if odd1 + even == even1 + odd:
                    ans += 1
                even1 += nums[i]
        return ans