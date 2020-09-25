# title: minimum-flips-to-make-a-or-b-equal-to-c
# detail: https://leetcode.com/submissions/detail/391419181/
# datetime: Sun Sep  6 01:07:30 2020
# runtime: 24 ms
# memory: 13.7 MB

class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        result = 0
        for i in range(31):
            i = a & 1
            j = b & 1
            k = c & 1
            if k != i | j:
                if k == 1:
                    result += 1
                else:
                    result += i + j
            a >>= 1
            b >>= 1
            c >>= 1
        return result