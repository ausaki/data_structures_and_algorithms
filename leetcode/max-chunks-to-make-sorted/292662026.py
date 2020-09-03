# title: max-chunks-to-make-sorted
# detail: https://leetcode.com/submissions/detail/292662026/
# datetime: Thu Jan  9 21:29:48 2020
# runtime: 28 ms
# memory: 12.8 MB

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        res = 0
        k = 0
        l = 1
        for i, num in enumerate(arr):
            l -= 1
            if num > k:
                l += num - k
                k = num
            elif l == 0:
                res += 1
                k += 1
                l = 1
        return res