# title: minimum-time-difference
# detail: https://leetcode.com/submissions/detail/286838921/
# datetime: Wed Dec 18 16:13:31 2019
# runtime: 68 ms
# memory: 20.9 MB

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minutes = sorted([int(h) * 60 + int(m) for h, m in [t.split(':') for t in timePoints]])
        return min(m2 - m1 for m1, m2 in zip(minutes, minutes[1:] + [minutes[0] + 24 * 60]))
        