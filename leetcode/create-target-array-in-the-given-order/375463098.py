# title: create-target-array-in-the-given-order
# detail: https://leetcode.com/submissions/detail/375463098/
# datetime: Mon Aug  3 23:48:35 2020
# runtime: 32 ms
# memory: 13.9 MB

class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        result = []
        for i, n in zip(index, nums):
            result.insert(i, n)
        return result
        