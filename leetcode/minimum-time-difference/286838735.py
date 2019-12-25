# title: minimum-time-difference
# detail: https://leetcode.com/submissions/detail/286838735/
# datetime: Wed Dec 18 16:12:22 2019
# runtime: 76 ms
# memory: 20.6 MB

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minutes = sorted([int(h) * 60 + int(m) for h, m in [t.split(':') for t in timePoints]])
        m = min([m2 - m1 for m1, m2 in zip(minutes[:-1], minutes[1:])])
        return min(m, minutes[0] + 24 * 60 - minutes[-1])
        