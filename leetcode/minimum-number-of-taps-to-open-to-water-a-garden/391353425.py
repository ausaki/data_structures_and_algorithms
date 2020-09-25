# title: minimum-number-of-taps-to-open-to-water-a-garden
# detail: https://leetcode.com/submissions/detail/391353425/
# datetime: Sat Sep  5 22:51:27 2020
# runtime: 216 ms
# memory: 15.1 MB

class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        ranges = [(i - r, i + r) for i, r in enumerate(ranges)]
        heapq.heapify(ranges)
        result = 0
        i = 0
        while i < n and ranges:
            maxr = -1
            while ranges and ranges[0][0] <= i:
                l, r = heapq.heappop(ranges)
                maxr = max(maxr, r)
            if maxr <= i:
                break
            i = maxr
            result += 1
        return result if i >= n else -1