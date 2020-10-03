# title: minimum-area-rectangle
# detail: https://leetcode.com/submissions/detail/403544435/
# datetime: Fri Oct  2 22:47:48 2020
# runtime: 640 ms
# memory: 31.6 MB

class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        points.sort()
        xs = collections.defaultdict(list)
        for x, y in points:
            xs[x].append(y)
        seen = {}
        result = math.inf
        for x, ylist in xs.items():
            for ys in itertools.combinations(ylist, 2):
                if ys in seen:
                    result = min(result, (x - seen[ys]) * (ys[1] - ys[0]))
                seen[ys] = x
        return 0 if math.isinf(result) else  result