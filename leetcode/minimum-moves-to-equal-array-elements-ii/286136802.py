# title: minimum-moves-to-equal-array-elements-ii
# detail: https://leetcode.com/submissions/detail/286136802/
# datetime: Sun Dec 15 22:14:32 2019
# runtime: 88 ms
# memory: 14 MB

class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        if not nums: return 0
        N = len(nums)
        nums.sort()
        y = nums[0]
        s1 = sum(num - y for num in nums)
        s2 = 0
        res = s1 + s2
        for i in range(1, N):
            dy = nums[i] - y
            s1 = s1 - (N - i) * dy
            s2 += dy * i
            y = nums[i]
            res = min(res, s1 + s2)
        return res