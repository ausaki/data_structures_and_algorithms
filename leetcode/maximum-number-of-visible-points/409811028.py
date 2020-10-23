# title: maximum-number-of-visible-points
# detail: https://leetcode.com/submissions/detail/409811028/
# datetime: Sat Oct 17 21:43:00 2020
# runtime: 1740 ms
# memory: 60 MB

class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        x0, y0 = location
        angles = []
        origin = 0
        for x, y in points:
            x -= x0
            y -= y0
            if x == 0 and y == 0:
                origin += 1
                continue
            ang = math.degrees(math.atan2(y, x))
            ang = (ang + 360) % 360
            angles.append(ang)
        angles.sort()
        result = 0
        for i, ang in enumerate(angles):
            ang2 = ang + angle
            j = bisect.bisect(angles, ang2, i)
            result = max(result, j - i)
            if ang2 > 360:
                k = bisect.bisect(angles, ang2 - 360)
                result = max(result, j - i + k)
        return result + origin
            
        