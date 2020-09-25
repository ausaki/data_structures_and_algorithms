# title: moving-stones-until-consecutive
# detail: https://leetcode.com/submissions/detail/400172216/
# datetime: Thu Sep 24 23:59:55 2020
# runtime: 24 ms
# memory: 13.8 MB

class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        if a > b:
            a, b = b, a
        if b > c:
            b, c = c, b
        if a > b:
            a, b = b, a
        min_, max_ = 0, c - a + 1 - 3
        if c - a + 1 == 3:
            min_ = 0
        elif b - a <= 2 or c - b <= 2:
            min_ = 1
        else:
            min_ = 2
        return [min_, max_]