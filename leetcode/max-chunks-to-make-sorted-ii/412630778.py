# title: max-chunks-to-make-sorted-ii
# detail: https://leetcode.com/submissions/detail/412630778/
# datetime: Sun Oct 25 00:33:23 2020
# runtime: 80 ms
# memory: 14.7 MB

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n = len(arr)
        pos = dict(zip(sorted(zip(arr, range(n))), range(n)))
        ma = (0, 0)
        result = 0
        for i, a in enumerate(arr):
            ma = max(ma, (a, i))
            if i == pos[ma]:
                result += 1
        return result