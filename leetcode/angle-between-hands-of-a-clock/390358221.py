# title: angle-between-hands-of-a-clock
# detail: https://leetcode.com/submissions/detail/390358221/
# datetime: Thu Sep  3 15:01:47 2020
# runtime: 32 ms
# memory: 13.7 MB

class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        h = (hour % 12 + minutes / 60) * 30
        m = minutes * 6
        a = abs(h - m)
        return a if a <= 180 else 360 - a