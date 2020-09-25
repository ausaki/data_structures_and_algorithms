# title: number-of-ways-where-square-of-number-is-equal-to-product-of-two-numbers
# detail: https://leetcode.com/submissions/detail/398397876/
# datetime: Mon Sep 21 02:13:09 2020
# runtime: 236 ms
# memory: 14 MB

class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        a = collections.Counter(nums1)
        ma = max(a)
        b = collections.Counter(nums2)
        mb = max(b)
        n = len(nums1)
        nums1.sort()
        m = len(nums2)
        nums2.sort()
        def cnt(nums, m, p):
            pp = p ** 2
            i = bisect.bisect_left(nums, p)
            result = 0
            for j in range(i):
                if pp % nums[j] == 0:
                    result += m[pp // nums[j]]
            i = m[p]
            return result + i * (i - 1) // 2
        return sum(cnt(nums2, b, i) for i in nums1) + sum(cnt(nums1, a, i) for i in nums2)
            