# title: design-underground-system
# detail: https://leetcode.com/submissions/detail/384483711/
# datetime: Sat Aug 22 12:21:06 2020
# runtime: 332 ms
# memory: 22.8 MB

class UndergroundSystem:

    def __init__(self):
        self.stations = {}
        self.times = collections.defaultdict(dict)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        if id in self.stations:
            return
        self.stations[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if id not in self.stations:
            return
        s, t0 = self.stations.pop(id)
        if stationName not in self.times[s]:
            self.times[s][stationName] = [0, 0]
        self.times[s][stationName][0] += t - t0
        self.times[s][stationName][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        t, c = self.times[startStation][endStation]
        return t / c


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)