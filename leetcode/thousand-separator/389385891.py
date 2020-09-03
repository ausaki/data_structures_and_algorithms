# title: thousand-separator
# detail: https://leetcode.com/submissions/detail/389385891/
# datetime: Tue Sep  1 18:54:24 2020
# runtime: 28 ms
# memory: 13.9 MB

class Solution:
    def thousandSeparator(self, n: int) -> str:
        return '{:,d}'.format(n).replace(',', '.')