# title: mirror-reflection
# detail: https://leetcode.com/submissions/detail/407411417/
# datetime: Mon Oct 12 01:02:44 2020
# runtime: 28 ms
# memory: 14.2 MB

class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        a, b, c, d = p, q, 1, -1
        mapper = [[2, 1], [1, 0], [0, -1], [-1, 2]]
        while True:
            if abs(b - p) <= 1e-3:
                return mapper[c][0 if d == -1 else 1]
            a, b = p - b, a / b * (p - b)
            c = (c + d) % 4
            while b - p >= 0.1:
                a, b = (b - p) / b * a, b - p
                d = -d
        return -1