# title: largest-triangle-area
# detail: https://leetcode.com/submissions/detail/410713000/
# datetime: Tue Oct 20 01:33:33 2020
# runtime: 328 ms
# memory: 14.1 MB

class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        result = 0
        for p1, p2, p3 in itertools.combinations(points, 3):
            x1, y1 = p2[0] - p1[0], p2[1] - p1[1]
            x2, y2 = p3[0] - p1[0], p3[1] - p1[1]
            a = math.sqrt(x1 ** 2 + y1 ** 2)
            b = math.sqrt(x2 ** 2 + y2 ** 2)
            cos = (x1 * x2 + y1 * y2) / (a * b)
            sin = math.sqrt(max(1 - cos ** 2, 0))
            result = max(result, a * b * sin / 2)
        return result