# title: robot-bounded-in-circle
# detail: https://leetcode.com/submissions/detail/399976685/
# datetime: Thu Sep 24 13:04:06 2020
# runtime: 32 ms
# memory: 14.1 MB

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        move = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        d = 1
        x, y = 0, 0
        for i in instructions:
            if i == 'G':
                x, y = x + move[d][0], y + move[d][1]
            else:
                d = (d + (1 if i == 'L' else -1)) % 4
        return d != 1 or (x == 0 and y == 0)
