# title: contiguous-array
# detail: https://leetcode.com/submissions/detail/287077368/
# datetime: Thu Dec 19 16:27:02 2019
# runtime: 904 ms
# memory: 17.1 MB

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        N = len(nums)
        ones = 0
        res = 0
        position = {0: -1}
        for i, v in enumerate(nums):
            if v == 1:
                ones += 1
            else:
                ones -= 1
            if ones in position:
                res = max(res, i - position[ones])
            else:
                position[ones] = i
        return res
                