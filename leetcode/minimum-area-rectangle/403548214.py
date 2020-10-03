# title: minimum-area-rectangle
# detail: https://leetcode.com/submissions/detail/403548214/
# datetime: Fri Oct  2 22:59:46 2020
# runtime: 2496 ms
# memory: 30.6 MB

class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        points.sort()
        n = len(points)
        result = math.inf
        seen = set()
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                if x2 == x1: continue
                a = (x1, y2, x2, y1)
                if a in seen:
                    result = min(result, (x2 - x1) * abs(y2 - y1))
                seen.add((x1, y1, x2, y2))
        return 0 if math.isinf(result) else result