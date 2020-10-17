# title: groups-of-special-equivalent-strings
# detail: https://leetcode.com/submissions/detail/405756984/
# datetime: Thu Oct  8 00:16:36 2020
# runtime: 36 ms
# memory: 14.6 MB

class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        c = collections.Counter(''.join(sorted(a[::2])) + ''.join(sorted(a[1::2])) for a in A)
        return len(c)