# title: create-target-array-in-the-given-order
# detail: https://leetcode.com/submissions/detail/375463353/
# datetime: Mon Aug  3 23:49:13 2020
# runtime: 36 ms
# memory: 14.1 MB

class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        result = []
        for i, n in enumerate(index):
            result.insert(n, nums[i])
        return result
        