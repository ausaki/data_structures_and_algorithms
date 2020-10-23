# title: maximum-number-of-visible-points
# detail: https://leetcode.com/submissions/detail/409813132/
# datetime: Sat Oct 17 21:52:06 2020
# runtime: 1600 ms
# memory: 59.9 MB

class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        x0, y0 = location
        angles = []
        origins = 0
        for x, y in points:
            x -= x0
            y -= y0
            if x == 0 and y == 0:
                origins += 1
                continue
            ang = (math.degrees(math.atan2(y, x)) + 360) % 360
            angles.append(ang)
        angles.sort()
        result = 0
        j, k = 0, 0
        n = len(angles)
        for i, ang in enumerate(angles):
            ang2 = ang + angle
            while j < n and angles[j] <= ang2:
                j += 1
            result = max(result, j - i)
            if ang2 > 360:
                ang2 -= 360
                while k < i and angles[k] <= ang2:
                    k += 1
                result = max(result, j - i + k)
        return result + origins
            
        