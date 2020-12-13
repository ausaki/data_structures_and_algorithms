# title: sum-of-absolute-differences-in-a-sorted-array
# detail: https://leetcode.com/submissions/detail/429867755/
# datetime: Sat Dec 12 22:45:09 2020
# runtime: 996 ms
# memory: 29.4 MB

class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        prev = 0
        for i in range(1, n):
            prev += (nums[i] - nums[i - 1]) * i
            res[i] += prev
        prev = 0
        for i in range(n - 2, -1, -1):
            prev += (nums[i + 1] - nums[i]) * (n - i - 1)
            res[i] += prev
        return res