# title: path-crossing
# detail: https://leetcode.com/submissions/detail/378854317/
# datetime: Mon Aug 10 20:48:46 2020
# runtime: 20 ms
# memory: 13.8 MB

class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited = {0: {0, }}
        x, y = 0, 0
        path_map = {'N': [0, 1], 'S': [0, -1], 'E': [1, 0], 'W': [-1, 0]}
        for p in path:
            if p == 'N':
                y += 1
            if p == 'S':
                y -= 1
            if p == 'E':
                x += 1
            if p == 'W':
                x -= 1
            if x in visited:
                if y in visited[x]:
                    return True
                visited[x].add(y)
            else:
                visited[x] = {y}
        return False