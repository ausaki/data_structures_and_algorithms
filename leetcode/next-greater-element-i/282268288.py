# title: next-greater-element-i
# detail: https://leetcode.com/submissions/detail/282268288/
# datetime: Thu Nov 28 20:31:42 2019
# runtime: 44 ms
# memory: 12.6 MB

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [-1] * len(nums1)
        pos = {n: i for i, n in enumerate(nums1)}
        stack = []
        for i in range(len(nums2)):
            while stack and nums2[i] > stack[-1]:
                n = stack.pop()
                if n in pos:
                    res[pos[n]] = nums2[i]
            stack.append(nums2[i])
        return res
        