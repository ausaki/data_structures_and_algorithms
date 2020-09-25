# title: number-of-ways-where-square-of-number-is-equal-to-product-of-two-numbers
# detail: https://leetcode.com/submissions/detail/398387223/
# datetime: Mon Sep 21 01:41:09 2020
# runtime: 536 ms
# memory: 14 MB

class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        a = collections.Counter(i * i for i in nums1)
        b = collections.Counter(i * i for i in nums2)
        n = len(nums1)
        m = len(nums2)
        result = 0
        for i in range(n):
            for j in range(i + 1, n):
                result += b[nums1[i] * nums1[j]]
        for i in range(m):
            for j in range(i + 1, m):
                result += a[nums2[i] * nums2[j]]
        return result