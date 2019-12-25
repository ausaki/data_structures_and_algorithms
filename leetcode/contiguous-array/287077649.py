# title: contiguous-array
# detail: https://leetcode.com/submissions/detail/287077649/
# datetime: Thu Dec 19 16:29:00 2019
# runtime: 928 ms
# memory: 17.1 MB

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        N = len(nums)
        ones = 0
        res = 0
        position = {0: -1}
        for i, v in enumerate(nums):
            ones += 1 if v else -1
            res = max(res, i - position.setdefault(ones, i))
        return res
                