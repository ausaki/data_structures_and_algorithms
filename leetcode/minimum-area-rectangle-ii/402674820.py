# title: minimum-area-rectangle-ii
# detail: https://leetcode.com/submissions/detail/402674820/
# datetime: Wed Sep 30 20:56:03 2020
# runtime: 1908 ms
# memory: 14 MB

class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        def test(p1, p2, p3):
            s = math.inf
            p4 = p1[0] + p3[0] - p2[0], p1[1] + p3[1] - p2[1]
            if p4 not in points:
                return s
            x1, y1 = p1[0] - p2[0], p1[1] - p2[1]
            x2, y2 = p2[0] - p3[0], p2[1] - p3[1]
            x3, y3 = p3[0] - p4[0], p3[1] - p4[1]
            x4, y4 = p4[0] - p1[0], p4[1] - p1[1]
            a1 = x1 * x2 + y1 * y2
            if a1 != 0: return s
            a2 = x2 * x3 + y2 * y3
            if a2 != 0: return s
            a3 = x3 * x4 + y3 * y4
            if a3 != 0: return s
            a4 = x4 * x1 + y4 * y1
            if a4 != 0: return s
            l1 = x1 ** 2 + y1 ** 2
            l2 = x2 ** 2 + y2 ** 2
            s = math.sqrt(l1) * math.sqrt(l2)
            return s
        points = set(map(tuple, points))
        s = min(test(*p) for p in itertools.permutations(points, 3))
        return 0 if math.isinf(s) else s
            
                