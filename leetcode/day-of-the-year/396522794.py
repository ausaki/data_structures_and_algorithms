# title: day-of-the-year
# detail: https://leetcode.com/submissions/detail/396522794/
# datetime: Wed Sep 16 17:53:11 2020
# runtime: 28 ms
# memory: 13.9 MB

class Solution:
    def dayOfYear(self, date: str) -> int:
        y, m, d = map(int, date.split('-'))
        M = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        d += sum(M[:m - 1])
        if m > 2 and ((y % 4 == 0 and y % 100 != 0) or y == 2000):
            d += 1
        return d
        