# title: escape-the-ghosts
# detail: https://leetcode.com/submissions/detail/293209168/
# datetime: Sat Jan 11 22:27:06 2020
# runtime: 56 ms
# memory: 12.8 MB

class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        distance = sum(map(abs, target))
        for x, y in ghosts:
            if abs(x - target[0]) + abs(y - target[1]) <= distance:
                return False
        return True