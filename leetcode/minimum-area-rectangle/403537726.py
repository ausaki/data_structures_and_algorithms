# title: minimum-area-rectangle
# detail: https://leetcode.com/submissions/detail/403537726/
# datetime: Fri Oct  2 22:25:50 2020
# runtime: 1096 ms
# memory: 14.4 MB

class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        points.sort()
        xs = collections.defaultdict(list)
        ys = collections.defaultdict(list)
        for x, y in points:
            xs[x].append(y)
            ys[y].append(x)
        result = math.inf
        for x0, ylist in xs.items():
            for y1, y2 in itertools.combinations(ylist, 2):
                xlist1, xlist2 = ys[y1], ys[y2]
                m, n = len(xlist1), len(xlist2)
                i = bisect.bisect(xlist1, x0)
                if i == m:
                    continue
                j = bisect.bisect(xlist2, x0)
                if j == n:
                    continue
                while i < m and j < n:
                    if xlist1[i] < xlist2[j]:
                        i += 1
                    elif xlist1[i] > xlist2[j]:
                        j += 1
                    else:
                        result = min(result, (xlist1[i] - x0) * (y2 - y1))
                        break
        return 0 if math.isinf(result) else  result