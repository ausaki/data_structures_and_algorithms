# title: minimum-number-of-refueling-stops
# detail: https://leetcode.com/submissions/detail/406849307/
# datetime: Sat Oct 10 16:07:08 2020
# runtime: 120 ms
# memory: 14.4 MB

class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        stations.append([target, 0])
        n = len(stations)
        q = []
        result = 0
        fuel = startFuel - stations[0][0]
        if fuel < 0:
            return -1
        for i, (p, l) in enumerate(stations):
            if i == n - 1:
                break
            heapq.heappush(q, -l)
            d = stations[i + 1][0] - p
            while q and fuel < d:
                fuel -= heapq.heappop(q)
                result += 1
            if fuel < d:
                return -1
            fuel -= d
        return result