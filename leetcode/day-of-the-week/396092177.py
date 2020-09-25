# title: day-of-the-week
# detail: https://leetcode.com/submissions/detail/396092177/
# datetime: Tue Sep 15 21:27:36 2020
# runtime: 40 ms
# memory: 13.7 MB

import datetime
class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        return ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"][datetime.date(year, month, day).weekday()]