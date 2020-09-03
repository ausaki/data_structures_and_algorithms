# title: escape-the-ghosts
# detail: https://leetcode.com/submissions/detail/293209221/
# datetime: Sat Jan 11 22:27:32 2020
# runtime: 44 ms
# memory: 12.8 MB

class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        distance = abs(target[0]) + abs(target[1])
        for x, y in ghosts:
            if abs(x - target[0]) + abs(y - target[1]) <= distance:
                return False
        return True