# title: find-nearest-point-that-has-the-same-x-or-y-coordinate
# detail: https://leetcode.com/submissions/detail/464242894/
# datetime: Sat Mar  6 22:33:52 2021
# runtime: 1300 ms
# memory: 19.4 MB

class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        res = -1
        dist = 10 ** 9
        for i, (a, b) in enumerate(points):
            if a == x or b == y:
                d = abs(a - x) + abs(b - y)
                if d < dist:
                    dist = d
                    res = i
        return res