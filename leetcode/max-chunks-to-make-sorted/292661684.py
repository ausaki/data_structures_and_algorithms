# title: max-chunks-to-make-sorted
# detail: https://leetcode.com/submissions/detail/292661684/
# datetime: Thu Jan  9 21:27:28 2020
# runtime: 28 ms
# memory: 12.6 MB

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        res = 0
        k = 0
        l = 1
        for i, num in enumerate(arr):
            if num > k:
                l += num - k - 1
                k = num
            else:
                l -= 1
                if l == 0:
                    res += 1
                    k += 1
                    l = 1
        return res