# title: check-if-one-string-swap-can-make-strings-equal
# detail: https://leetcode.com/submissions/detail/467520450/
# datetime: Sun Mar 14 12:42:22 2021
# runtime: 32 ms
# memory: 14.2 MB

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        s = 0
        c, d = '', ''
        for a, b in zip(s1, s2):
            s += a != b
            if s > 2:
                return False
            if a != b:
                if c == '':
                    c, d = a, b
                else:
                    if not (a == d and b == c):
                        return False
        return s == 0 or s == 2