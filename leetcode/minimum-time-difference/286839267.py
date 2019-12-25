# title: minimum-time-difference
# detail: https://leetcode.com/submissions/detail/286839267/
# datetime: Wed Dec 18 16:15:29 2019
# runtime: 96 ms
# memory: 15.8 MB

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minutes = sorted([int(t[:2]) * 60 + int(t[3:]) for t in timePoints])
        return min(m2 - m1 for m1, m2 in zip(minutes, minutes[1:] + [minutes[0] + 24 * 60]))
        