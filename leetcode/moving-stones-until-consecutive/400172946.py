# title: moving-stones-until-consecutive
# detail: https://leetcode.com/submissions/detail/400172946/
# datetime: Fri Sep 25 00:01:57 2020
# runtime: 24 ms
# memory: 14 MB

class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        a, b, c = sorted([a, b, c])
        min_, max_ = 2, c - a + 1 - 3
        if c - a + 1 == 3:
            min_ = 0
        elif b - a <= 2 or c - b <= 2:
            min_ = 1
        return [min_, max_]