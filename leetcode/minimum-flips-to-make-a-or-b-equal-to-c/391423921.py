# title: minimum-flips-to-make-a-or-b-equal-to-c
# detail: https://leetcode.com/submissions/detail/391423921/
# datetime: Sun Sep  6 01:20:49 2020
# runtime: 28 ms
# memory: 13.9 MB

class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        x = (a | b) ^ c
        return bin(x & c).count('1') + bin(x & a).count('1') + bin(x & b).count('1')
