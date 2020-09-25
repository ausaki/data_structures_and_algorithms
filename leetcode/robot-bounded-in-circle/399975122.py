# title: robot-bounded-in-circle
# detail: https://leetcode.com/submissions/detail/399975122/
# datetime: Thu Sep 24 13:00:09 2020
# runtime: 32 ms
# memory: 13.8 MB

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        deg = {'R': -90, 'L': 90}
        d = 90
        x, y = 0, 0
        for i in instructions:
            if i == 'G':
                if d == 90:
                    y += 1
                elif d == 270:
                    y -= 1
                elif d == 0:
                    x += 1
                else:
                    x -= 1
            else:
                d = (d + deg[i]) % 360
        return d != 90 or (x == 0 and y == 0)
