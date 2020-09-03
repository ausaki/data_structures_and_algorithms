# title: destination-city
# detail: https://leetcode.com/submissions/detail/382656027/
# datetime: Tue Aug 18 18:51:59 2020
# runtime: 56 ms
# memory: 13.9 MB

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        g = {}
        for a, b in paths:
            g[a] = b
        c = a
        while c in g:
            c = g[c]
        return c
