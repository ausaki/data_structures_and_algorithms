# title: minimum-number-of-refueling-stops
# detail: https://leetcode.com/submissions/detail/406854757/
# datetime: Sat Oct 10 16:28:14 2020
# runtime: 1028 ms
# memory: 14.3 MB

class Solution(object):
    def minRefuelStops(self, target, startFuel, stations):
        dp = [startFuel] + [0] * len(stations)
        for i, (location, capacity) in enumerate(stations):
            for t in range(i, -1, -1):
                if dp[t] >= location:
                    dp[t+1] = max(dp[t+1], dp[t] + capacity)

        for i, d in enumerate(dp):
            if d >= target: return i
        return -1