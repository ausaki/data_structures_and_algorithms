# title: minimum-number-of-taps-to-open-to-water-a-garden
# detail: https://leetcode.com/submissions/detail/391373003/
# datetime: Sat Sep  5 23:24:42 2020
# runtime: 148 ms
# memory: 14.4 MB

class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        new_ranges = [0] * (n + 1)
        for i, j in enumerate(ranges):
            l, r = max(i - j, 0), i + j
            new_ranges[l] = max(new_ranges[l], r)
        result = 0
        i = 0
        j = 0
        while i < n and j <= n:
            maxr = -1
            for k in range(j, i + 1):
                maxr = max(maxr, new_ranges[k])
            if maxr <= i:
                break
            j = i + 1
            i = maxr
            result += 1
        return result if i >= n else -1