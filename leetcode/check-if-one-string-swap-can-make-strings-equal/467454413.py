# title: check-if-one-string-swap-can-make-strings-equal
# detail: https://leetcode.com/submissions/detail/467454413/
# datetime: Sun Mar 14 10:34:28 2021
# runtime: 24 ms
# memory: 14.4 MB

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        s = sum(1 for a, b in zip(s1, s2) if a != b)
        
        return (s == 0 or s == 2) and (sorted(s1) == sorted(s2))