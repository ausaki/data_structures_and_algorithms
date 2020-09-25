# title: distance-between-bus-stops
# detail: https://leetcode.com/submissions/detail/396089901/
# datetime: Tue Sep 15 21:20:07 2020
# runtime: 52 ms
# memory: 14.8 MB

class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        s1 = sum(distance[min(start, destination):max(start, destination)])
        return min(s1, sum(distance) - s1)