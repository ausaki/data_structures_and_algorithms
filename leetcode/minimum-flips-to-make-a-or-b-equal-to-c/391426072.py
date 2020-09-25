# title: minimum-flips-to-make-a-or-b-equal-to-c
# detail: https://leetcode.com/submissions/detail/391426072/
# datetime: Sun Sep  6 01:26:48 2020
# runtime: 32 ms
# memory: 13.9 MB

class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        def bitcount(x):
            c = 0
            while x:
                x &= x - 1
                c += 1
            return c
        x = (a | b) ^ c
        return bitcount(x) + bitcount(x & (a & b))
