# title: number-of-days-between-two-dates
# detail: https://leetcode.com/submissions/detail/386672265/
# datetime: Wed Aug 26 22:48:37 2020
# runtime: 28 ms
# memory: 13.9 MB

import datetime
class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        d1 = datetime.date.fromisoformat(date1)
        d2 = datetime.date.fromisoformat(date2)
        d = d1 - d2
        return abs(d.days)