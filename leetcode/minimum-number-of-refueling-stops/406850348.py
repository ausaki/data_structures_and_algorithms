# title: minimum-number-of-refueling-stops
# detail: https://leetcode.com/submissions/detail/406850348/
# datetime: Sat Oct 10 16:10:58 2020
# runtime: 116 ms
# memory: 14.2 MB

class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        stations.append([target, 0])
        stations.insert(0, [0, 0])
        n = len(stations)
        q = []
        result = 0
        for i in range(n - 1):
            heapq.heappush(q, -stations[i][1])
            d = stations[i + 1][0] - stations[i][0]
            while q and startFuel < d:
                startFuel -= heapq.heappop(q)
                result += 1
            if startFuel < d:
                return -1
            startFuel -= d
        return result