# title: water-and-jug-problem
# detail: https://leetcode.com/submissions/detail/367701675/
# datetime: Fri Jul 17 11:59:05 2020
# runtime: 44 ms
# memory: 13.7 MB

class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        def gcd(a, b):
            while b > 0:
                a, b = b, a % b
            return a
        
        if z == 0:
            return True
        if z > x + y:
            return False
        g = gcd(x, y)
        return z % g == 0
            