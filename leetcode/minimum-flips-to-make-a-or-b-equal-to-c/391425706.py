# title: minimum-flips-to-make-a-or-b-equal-to-c
# detail: https://leetcode.com/submissions/detail/391425706/
# datetime: Sun Sep  6 01:25:44 2020
# runtime: 20 ms
# memory: 14 MB

class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        x = (a | b) ^ c
        return bin(x).count('1') + bin(x & (a & b)).count('1')
