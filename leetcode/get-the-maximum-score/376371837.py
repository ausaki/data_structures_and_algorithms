# title: get-the-maximum-score
# detail: https://leetcode.com/submissions/detail/376371837/
# datetime: Wed Aug  5 15:16:46 2020
# runtime: 648 ms
# memory: 25.6 MB

class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        m = len(nums2)
        MOD = 10 ** 9 + 7
        i = n - 1
        j = m - 1
        sum1 = 0
        sum2 = 0
        max_sum = 0
        while i >= 0 and j >= 0:
            while i >= 0 and nums1[i] > nums2[j]:
                sum1 += nums1[i]
                i -= 1
            if i < 0:
                break
            while j >= 0 and nums2[j] > nums1[i]:
                sum2 += nums2[j]
                j -= 1
            if j < 0:
                break
            if nums1[i] == nums2[j]:
                sum1 += nums1[i]
                sum2 += nums2[j]
                # print(nums1[i], sum1, sum2, max_sum)
                max_sum += max(sum1, sum2)
                sum1 = sum2 = 0
                i -= 1
                j -= 1
        if i >= 0:
            sum1 += sum(nums1[:i + 1])
            max_sum += max(sum1, sum2)
        if j >= 0:
            sum2 += sum(nums2[:j + 1])
            max_sum += max(sum1, sum2)
        return max_sum % MOD
            