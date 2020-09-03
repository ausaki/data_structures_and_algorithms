# title: maximum-product-of-two-elements-in-an-array
# detail: https://leetcode.com/submissions/detail/381241412/
# datetime: Sat Aug 15 22:43:07 2020
# runtime: 92 ms
# memory: 13.9 MB

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        a, b = heapq.nlargest(2, (a - 1 for a in nums), key=lambda a: a - 1)
        return a * b