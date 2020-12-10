# title: max-chunks-to-make-sorted
# detail: https://leetcode.com/submissions/detail/412620377/
# datetime: Sat Oct 24 23:54:48 2020
# runtime: 36 ms
# memory: 14.3 MB

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        k = 0
        result = 0
        for i, a in enumerate(arr):
            k = max(k, a)
            if k == i:
                result += 1
        return result