# title: number-of-different-subsequences-gcds
# detail: https://leetcode.com/submissions/detail/476205809/
# datetime: Sun Apr  4 12:12:15 2021
# runtime: 9736 ms
# memory: 34.4 MB

class Solution:
    def countDifferentSubsequenceGCDs(self, nums: List[int]) -> int:
        ma = max(nums) + 1
        nums = set(nums)
        res = 0
        for i in range(1, ma):
            g = 0
            for j in range(i, ma, i):
                if j in nums:
                    g = math.gcd(g, j)
            if g == i:
                res += 1
        return res
                    