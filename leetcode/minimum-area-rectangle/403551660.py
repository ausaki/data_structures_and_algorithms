# title: minimum-area-rectangle
# detail: https://leetcode.com/submissions/detail/403551660/
# datetime: Fri Oct  2 23:10:46 2020
# runtime: 1768 ms
# memory: 14.5 MB

class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        maps = set(map(tuple, points))
        points.sort()
        n = len(points)
        result = math.inf
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                if x2 == x1 or y1 == y2: continue
                if (x1, y2) in maps and (x2, y1) in maps:
                    result = min(result, (x2 - x1) * abs(y2 - y1))
        return 0 if math.isinf(result) else result