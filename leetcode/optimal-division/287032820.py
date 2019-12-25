# title: optimal-division
# detail: https://leetcode.com/submissions/detail/287032820/
# datetime: Thu Dec 19 12:47:04 2019
# runtime: 28 ms
# memory: 12.7 MB

class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        if len(nums) <= 2: return '/'.join(map(str, nums))
        return str(nums[0]) + '/(' +  '/'.join(map(str, nums[1:])) + ')'