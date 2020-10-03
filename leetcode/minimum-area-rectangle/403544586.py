# title: minimum-area-rectangle
# detail: https://leetcode.com/submissions/detail/403544586/
# datetime: Fri Oct  2 22:48:17 2020
# runtime: 684 ms
# memory: 31.8 MB

class Solution(object):
    def minAreaRect(self, points):
        xrange = range
        columns = collections.defaultdict(list)
        for x, y in points:
            columns[x].append(y)
        lastx = {}
        ans = float('inf')

        for x in sorted(columns):
            column = columns[x]
            column.sort()
            for j, y2 in enumerate(column):
                for i in xrange(j):
                    y1 = column[i]
                    if (y1, y2) in lastx:
                        ans = min(ans, (x - lastx[y1,y2]) * (y2 - y1))
                    lastx[y1, y2] = x
        return ans if ans < float('inf') else 0