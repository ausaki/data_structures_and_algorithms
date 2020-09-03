# title: maximum-product-of-two-elements-in-an-array
# detail: https://leetcode.com/submissions/detail/381241113/
# datetime: Sat Aug 15 22:42:13 2020
# runtime: 56 ms
# memory: 13.8 MB

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        a, b = heapq.nlargest(2, nums, key=lambda a: a - 1)
        return (a - 1) * (b - 1)