# title: generate-random-point-in-a-circle
# detail: https://leetcode.com/submissions/detail/286378197/
# datetime: Mon Dec 16 21:11:39 2019
# runtime: 140 ms
# memory: 23 MB

import math
import random
class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center

    def randPoint(self) -> List[float]:
        '''极坐标'''
        radian = random.random() * math.pi * 2
        radius = math.sqrt(random.random() * self.radius ** 2)
        x = radius * math.cos(radian)
        y = radius * math.sin(radian)
        return [x + self.x_center, y + self.y_center]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()