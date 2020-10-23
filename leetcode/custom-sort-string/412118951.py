# title: custom-sort-string
# detail: https://leetcode.com/submissions/detail/412118951/
# datetime: Fri Oct 23 11:55:49 2020
# runtime: 32 ms
# memory: 14.1 MB

class Solution:
    def customSortString(self, S: str, T: str) -> str:
        pos = {c: i for i, c in enumerate(S)}
        return ''.join(sorted(T, key=lambda k: pos.get(k, -1)))