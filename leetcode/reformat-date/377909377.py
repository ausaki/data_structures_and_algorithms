# title: reformat-date
# detail: https://leetcode.com/submissions/detail/377909377/
# datetime: Sat Aug  8 23:09:58 2020
# runtime: 32 ms
# memory: 13.8 MB

class Solution:
    def reformatDate(self, date: str) -> str:
        d, m, y = date.split(' ')
        month_map = dict(zip(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"], range(1, 13)))
        return '{0}-{1:02d}-{2:>02s}'.format(y, month_map[m], d[:-2])