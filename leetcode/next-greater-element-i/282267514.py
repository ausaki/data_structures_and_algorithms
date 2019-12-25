# title: next-greater-element-i
# detail: https://leetcode.com/submissions/detail/282267514/
# datetime: Thu Nov 28 20:22:56 2019
# runtime: 44 ms
# memory: 12.8 MB

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [-1] * len(nums1)
        pos = {n: i for i, n in enumerate(nums2)}
        for i in range(len(nums1)):
            for j in range(pos[nums1[i]] + 1, len(nums2)):
                if nums2[j] > nums1[i]:
                    res[i] = nums2[j]
                    break
        return res
        