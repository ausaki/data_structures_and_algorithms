# title: minimum-swaps-to-make-strings-equal
# detail: https://leetcode.com/submissions/detail/394525021/
# datetime: Sat Sep 12 16:00:51 2020
# runtime: 32 ms
# memory: 13.9 MB

class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        xy, yx = 0, 0
        for i, j in zip(s1, s2):
            xy += i == 'x' and j == 'y'
            yx += i == 'y' and j == 'x'
        x, r1 = divmod(xy, 2)
        y, r2 = divmod(yx, 2)
        if r1 + r2 == 2:
            x += 2
        elif r1 + r2 == 1:
            return -1
        return x + y
        