# title: max-chunks-to-make-sorted
# detail: https://leetcode.com/submissions/detail/412619699/
# datetime: Sat Oct 24 23:52:15 2020
# runtime: 32 ms
# memory: 14.1 MB

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        k = 0
        result = 0
        for i, a in enumerate(arr):
            if a > k:
                k = a
            elif k == i:
                result += 1
                k = i + 1
        return result