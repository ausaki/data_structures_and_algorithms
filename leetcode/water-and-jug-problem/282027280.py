# title: water-and-jug-problem
# detail: https://leetcode.com/submissions/detail/282027280/
# datetime: Wed Nov 27 16:45:44 2019
# runtime: 80 ms
# memory: 12.8 MB

class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        if z == 0:
            return True
        if z > x + y:
            return False
        if x > y:
            x, y = y, x
        if z == y:
            return True
        b = x
        while b != 0:
            if z == b or (b <= x and z == b + y):
                return True
            b = (b + x) % y
        return False