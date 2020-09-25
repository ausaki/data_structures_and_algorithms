# title: distance-between-bus-stops
# detail: https://leetcode.com/submissions/detail/396090844/
# datetime: Tue Sep 15 21:23:12 2020
# runtime: 76 ms
# memory: 14.8 MB

class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        s, d = min(start, destination), max(start, destination)
        s0, s1 = 0, 0
        for i, dis in enumerate(distance):
            if s <= i < d:
                s0 += dis
            else:
                s1 += dis
        return min(s0, s1)
