# title: random-pick-index
# detail: https://leetcode.com/submissions/detail/285389092/
# datetime: Thu Dec 12 11:28:49 2019
# runtime: 304 ms
# memory: 16.7 MB

import random
class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        k = 0
        res = -1
        for i, num in enumerate(self.nums):
            if num == target:
                k += 1
                if random.random() < 1 / k:
                    res = i
        return res


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)