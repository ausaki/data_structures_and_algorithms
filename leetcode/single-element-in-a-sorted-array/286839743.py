# title: single-element-in-a-sorted-array
# detail: https://leetcode.com/submissions/detail/286839743/
# datetime: Wed Dec 18 16:18:26 2019
# runtime: 76 ms
# memory: 14.9 MB

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res ^= num
        return res