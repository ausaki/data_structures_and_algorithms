# title: max-chunks-to-make-sorted
# detail: https://leetcode.com/submissions/detail/292662115/
# datetime: Thu Jan  9 21:30:22 2020
# runtime: 20 ms
# memory: 12.6 MB

class Solution(object):
    def maxChunksToSorted(self, arr):
        ans = ma = 0
        for i, x in enumerate(arr):
            ma = max(ma, x)
            if ma == i: ans += 1
        return ans