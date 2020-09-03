# title: maximum-product-of-two-elements-in-an-array
# detail: https://leetcode.com/submissions/detail/381241663/
# datetime: Sat Aug 15 22:43:54 2020
# runtime: 60 ms
# memory: 13.7 MB

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        a, b = heapq.nlargest(2, nums)
        return (a - 1) * (b - 1)