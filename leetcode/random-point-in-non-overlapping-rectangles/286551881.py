# title: random-point-in-non-overlapping-rectangles
# detail: https://leetcode.com/submissions/detail/286551881/
# datetime: Tue Dec 17 13:11:22 2019
# runtime: 164 ms
# memory: 16.6 MB

import random
import bisect
class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.areas = []
        a = 0
        for x1, y1, x2, y2 in self.rects:
            a += (x2 - x1 + 1) * (y2 - y1 + 1) 
            self.areas.append(a)
        self.total_area = a
        
    def pick(self) -> List[int]:
        area = random.randint(0, self.total_area - 1)
        i = bisect.bisect(self.areas, area)
        area -= self.areas[i - 1] if i > 0 else 0
        x1, y1, x2, y2 = self.rects[i]
        x = x1 + area % (x2 - x1 + 1) 
        y = y1 + area // (x2 - x1 + 1)
        return [x, y]

# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()
