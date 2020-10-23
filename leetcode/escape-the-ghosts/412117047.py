# title: escape-the-ghosts
# detail: https://leetcode.com/submissions/detail/412117047/
# datetime: Fri Oct 23 11:49:57 2020
# runtime: 44 ms
# memory: 14.1 MB

class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        dist = abs(target[0]) + abs(target[1])
        for x, y in ghosts:
            d = abs(x - target[0]) + abs(y - target[1])
            if d <= dist:
                return False
        return True