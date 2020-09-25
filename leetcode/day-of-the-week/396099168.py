# title: day-of-the-week
# detail: https://leetcode.com/submissions/detail/396099168/
# datetime: Tue Sep 15 21:48:43 2020
# runtime: 28 ms
# memory: 14 MB

import datetime
class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        Y, M, D, W = 1971, 1, 1, 4
        WEEK = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        MDAYS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
        isleap = lambda y: (y % 4 == 0 and y % 100 != 0) or y == 2000
        days = 0
        for y in range(Y, year):
            days += 365
            if isleap(y):
                days += 1
        l = isleap(year)
        for m in range(month - 1):
            days += MDAYS[m]
            if l and m == 1:
                days += 1
        days += day - 1
        return WEEK[(W + days) % 7]
