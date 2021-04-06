# title: find-nearest-point-that-has-the-same-x-or-y-coordinate
# detail: https://leetcode.com/submissions/detail/464293867/
# datetime: Sun Mar  7 00:27:14 2021
# runtime: 900 ms
# memory: 19.6 MB

class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        res = -1
        dist = 10 ** 9
        return min(((abs(a - x) + abs(b - y), i)  for i, (a, b) in enumerate(points) if a == x or b == y), default=(-1, -1))[1]
