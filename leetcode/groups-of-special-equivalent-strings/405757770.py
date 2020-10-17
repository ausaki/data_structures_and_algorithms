# title: groups-of-special-equivalent-strings
# detail: https://leetcode.com/submissions/detail/405757770/
# datetime: Thu Oct  8 00:18:59 2020
# runtime: 32 ms
# memory: 14.3 MB

class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        return len(set(''.join(sorted(a[::2])) + ''.join(sorted(a[1::2])) for a in A))
