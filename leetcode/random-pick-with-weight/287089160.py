# title: random-pick-with-weight
# detail: https://leetcode.com/submissions/detail/287089160/
# datetime: Thu Dec 19 17:55:28 2019
# runtime: 224 ms
# memory: 17.5 MB

import random
import bisect
class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        self.ranges = [0] * len(self.w)
        weight = 0
        for i, w in enumerate(self.w):
            weight += w
            self.ranges[i] = weight
        self.total_weight = weight
        
    def pickIndex(self) -> int:
        x = random.randrange(0, self.total_weight)
        i = bisect.bisect(self.ranges, x)
        return i


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()