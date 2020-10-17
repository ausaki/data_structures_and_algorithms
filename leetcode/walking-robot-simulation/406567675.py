# title: walking-robot-simulation
# detail: https://leetcode.com/submissions/detail/406567675/
# datetime: Fri Oct  9 22:02:31 2020
# runtime: 420 ms
# memory: 19.8 MB

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        x, y = 0, 0
        d = 1
        result = 0
        dxy = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        obstacles = set(map(tuple, obstacles))
        for c in commands:
            if c == -2:
                d = (d + 1) % 4
            elif c == -1:
                d = (d - 1) % 4
            else:
                for i in range(c):
                    if (x + dxy[d][0], y + dxy[d][1]) in obstacles:
                        break
                    x += dxy[d][0]
                    y += dxy[d][1]
                    result = max(result, x ** 2 + y ** 2)
        return result
        