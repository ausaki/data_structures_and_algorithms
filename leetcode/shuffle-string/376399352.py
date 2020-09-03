# title: shuffle-string
# detail: https://leetcode.com/submissions/detail/376399352/
# datetime: Wed Aug  5 16:40:38 2020
# runtime: 108 ms
# memory: 13.9 MB

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        l = [None] * len(s)
        for c, i in zip(s, indices):
            l[i] = c
        return ''.join(l)