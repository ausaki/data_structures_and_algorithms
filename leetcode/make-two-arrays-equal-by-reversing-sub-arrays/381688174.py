# title: make-two-arrays-equal-by-reversing-sub-arrays
# detail: https://leetcode.com/submissions/detail/381688174/
# datetime: Sun Aug 16 19:10:56 2020
# runtime: 76 ms
# memory: 14 MB

class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        target.sort()
        arr.sort()
        return target == arr