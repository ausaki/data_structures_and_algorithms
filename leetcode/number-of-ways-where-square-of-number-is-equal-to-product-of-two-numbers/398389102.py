# title: number-of-ways-where-square-of-number-is-equal-to-product-of-two-numbers
# detail: https://leetcode.com/submissions/detail/398389102/
# datetime: Mon Sep 21 01:46:44 2020
# runtime: 584 ms
# memory: 13.9 MB

class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        a = collections.Counter(i * i for i in nums1)
        ma = max(a)
        b = collections.Counter(i * i for i in nums2)
        mb = max(b)
        n = len(nums1)
        nums1.sort()
        m = len(nums2)
        nums2.sort()
        result = 0
        for i in range(n):
            for j in range(i + 1, n):
                p = nums1[i] * nums1[j]
                result += b[p]
                if p > mb:
                    break
        for i in range(m):
            for j in range(i + 1, m):
                p = nums2[i] * nums2[j]
                result += a[p]
                if p > ma:
                    break
        return result