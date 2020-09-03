# title: make-two-arrays-equal-by-reversing-sub-arrays
# detail: https://leetcode.com/submissions/detail/381687329/
# datetime: Sun Aug 16 19:07:20 2020
# runtime: 88 ms
# memory: 14.1 MB

class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return collections.Counter(target) == collections.Counter(arr)