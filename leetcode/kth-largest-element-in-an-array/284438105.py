# title: kth-largest-element-in-an-array
# detail: https://leetcode.com/submissions/detail/284438105/
# datetime: Sun Dec  8 10:26:04 2019
# runtime: 64 ms
# memory: 13.5 MB

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums, reverse=True)[k - 1]