# title: reverse-subarray-to-maximize-array-value
# detail: https://leetcode.com/submissions/detail/391270819/
# datetime: Sat Sep  5 17:51:51 2020
# runtime: 316 ms
# memory: 17.7 MB

class Solution:
    def maxValueAfterReverse(self, nums: List[int]) -> int:
        n = len(nums)
        s0 = 0
        s1 = 0
        minp, maxp = 1e9, -1e9
        for i in range(n - 1):
            a, b = nums[i], nums[i + 1]
            ab = abs(a - b)
            s0 += ab
            s1 = max(s1, abs(b - nums[0]) - ab)
            s1 = max(s1, abs(a - nums[-1]) - ab)
            minp, maxp = min(minp, max(a, b)), max(maxp, min(a, b))
        return s0 + max(s1, 2 * (maxp - minp))
                