# title: valid-boomerang
# detail: https://leetcode.com/submissions/detail/400092185/
# datetime: Thu Sep 24 19:19:00 2020
# runtime: 64 ms
# memory: 13.9 MB

class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        a, b = 1000, 1000
        if points[0] == points[1] or points[0] == points[2] or points[1] == points[2]:
            return False
        if points[0][0] == points[1][0]:
            return points[2][0] != points[0][0]
        if points[0][0] == points[2][0]:
            return points[1][0] != points[0][0]
        return (points[0][1] - points[1][1]) * (points[0][0] - points[2][0]) != (points[0][1] - points[2][1]) * (points[0][0] - points[1][0])
