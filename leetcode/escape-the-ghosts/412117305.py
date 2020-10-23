# title: escape-the-ghosts
# detail: https://leetcode.com/submissions/detail/412117305/
# datetime: Fri Oct 23 11:50:48 2020
# runtime: 48 ms
# memory: 14.2 MB

class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        dist = abs(target[0]) + abs(target[1])
        return all(abs(x - target[0]) + abs(y - target[1]) > dist for x, y in ghosts)
