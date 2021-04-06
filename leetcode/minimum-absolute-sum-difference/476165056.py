# title: minimum-absolute-sum-difference
# detail: https://leetcode.com/submissions/detail/476165056/
# datetime: Sun Apr  4 10:50:11 2021
# runtime: 2556 ms
# memory: 37.3 MB

class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        s = sum(abs(a - b) for a, b in zip(nums1, nums2))
        A = sorted(zip(nums1, range(n)))
        res = s
        for a, i in A:
            b = nums2[i]
            j = bisect.bisect(A, (b, 10 ** 6))
            if j < n:
                res = min(res, s - abs(a - b) + abs(A[j][0] - b))
            if j > 0:
                res = min(res, s - abs(a - b) + abs(A[j - 1][0] - b))
        return res % (10 ** 9 + 7)