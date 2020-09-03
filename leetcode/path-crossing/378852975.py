# title: path-crossing
# detail: https://leetcode.com/submissions/detail/378852975/
# datetime: Mon Aug 10 20:43:53 2020
# runtime: 32 ms
# memory: 14.1 MB

class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited = {(0, 0)}
        pos = (0, 0)
        path_map = {'N': [0, 1], 'S': [0, -1], 'E': [1, 0], 'W': [-1, 0]}
        for p in path:
            dx, dy = path_map[p]
            pos = (pos[0] + dx, pos[1] + dy)
            if pos in visited:
                return True
            visited.add(pos)
        return False