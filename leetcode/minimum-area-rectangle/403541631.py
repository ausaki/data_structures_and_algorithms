# title: minimum-area-rectangle
# detail: https://leetcode.com/submissions/detail/403541631/
# datetime: Fri Oct  2 22:38:55 2020
# runtime: 420 ms
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
            for i in range(len(ylist)):
                y1 = ylist[i]
                xlist1 = ys[y1]
                m = len(xlist1)
                ii = bisect.bisect(xlist1, x0)
                if ii == m:
                    continue
                for j in range(i + 1, len(ylist)):
                    y2 = ylist[j]
                    xlist2 = ys[y2]
                    n = len(xlist2)
                    jj = bisect.bisect(xlist2, x0)
                    if jj == n:
                        continue
                    i1 = ii
                    while i1 < m and jj < n:
                        if xlist1[i1] < xlist2[jj]:
                            i1 += 1
                        elif xlist1[i1] > xlist2[jj]:
                            jj += 1
                        else:
                            result = min(result, (xlist1[i1] - x0) * (y2 - y1))
                            break
        return 0 if math.isinf(result) else  result