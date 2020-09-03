# title: maximum-product-of-two-elements-in-an-array
# detail: https://leetcode.com/submissions/detail/381241507/
# datetime: Sat Aug 15 22:43:24 2020
# runtime: 68 ms
# memory: 13.9 MB

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        a, b = heapq.nlargest(2, (a - 1 for a in nums))
        return a * b