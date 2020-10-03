# title: minimum-area-rectangle-ii
# detail: https://leetcode.com/submissions/detail/402683386/
# datetime: Wed Sep 30 21:29:37 2020
# runtime: 108 ms
# memory: 14.5 MB

class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        n = len(points)
        new_points = collections.defaultdict(list)
        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                l = (x1 - x2) ** 2 + (y1 - y2) ** 2
                x0, y0 = (x1 + x2) / 2, (y1 + y2) / 2
                new_points[(l, x0, y0)].append((i, j))
        result = math.inf
        for ps in new_points.values():
            m = len(ps)
            for i in range(m):
                for j in range(i + 1, m):
                    x1, y1 = points[ps[i][0]]
                    x2, y2 = points[ps[i][1]]
                    x3, y3 = points[ps[j][0]]
                    l1 = math.sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2)
                    l2 = math.sqrt((x2 - x3) ** 2 + (y2 - y3) ** 2)
                    print(l1, l2)
                    result = min(result, l1 * l2)
        return 0 if math.isinf(result) else result
                