# title: valid-square
# detail: https://leetcode.com/submissions/detail/287328822/
# datetime: Fri Dec 20 20:18:10 2019
# runtime: 32 ms
# memory: 12.8 MB

import math
class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        dist = lambda a, b: math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)
        angle = lambda a, b: a[1] - b[1] / (a[0] - b[0])
        dotmul = lambda v1, v2: v1[0] * v2[0] + v1[1] * v2[1]
        p2[0] -= p1[0]
        p2[1] -= p1[1]
        p3[0] -= p1[0]
        p3[1] -= p1[1]
        p4[0] -= p1[0]
        p4[1] -= p1[1]
        p1[0] = 0
        p1[1] = 0
        print(p1, p2, p3, p4)
        d2 = p2[0] ** 2 + p2[1] ** 2
        d3 = p3[0] ** 2 + p3[1] ** 2
        d4 = p4[0] ** 2 + p4[1] ** 2
        if d2 == 0 or d3 == 0 or d4 == 0:
            return False
        if d2 == d4:
            p3, p4 = p4, p3
            d3, d4 = d4, d3
        elif d3 == d4:
            p2, p4 = p4, p2
            d2, d4 = d4, d2
        elif d2 == d3:
            pass
        else:
            return False
        if d4 != d2 + d3:
            return False
        if dotmul(p2, p3) != 0:
            return False
        return p2[0] + p3[0] == p4[0] and p2[1] + p3[1] == p4[1]
        
        
        