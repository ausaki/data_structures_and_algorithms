# title: check-if-it-is-a-good-array
# detail: https://leetcode.com/submissions/detail/394551412/
# datetime: Sat Sep 12 17:47:41 2020
# runtime: 288 ms
# memory: 24.4 MB

class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        n = len(nums)
        g = nums[0]
        for i in range(1, n):
            g = math.gcd(g, nums[i])
        return g == 1