# title: groups-of-special-equivalent-strings
# detail: https://leetcode.com/submissions/detail/405757051/
# datetime: Thu Oct  8 00:16:48 2020
# runtime: 44 ms
# memory: 14.3 MB

class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        return len(collections.Counter(''.join(sorted(a[::2])) + ''.join(sorted(a[1::2])) for a in A))
