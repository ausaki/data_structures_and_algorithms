# title: minimum-number-of-refueling-stops
# detail: https://leetcode.com/submissions/detail/406854552/
# datetime: Sat Oct 10 16:27:24 2020
# runtime: 2644 ms
# memory: 14.8 MB

class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        n = len(stations)
        if startFuel >= target:
            return 0
        dp = [0] * (n + 1)
        dp[0] = startFuel
        result = n + 1
        for i in range(n):
            p, l = stations[i]
            for j in range(i, -1, -1):
                if dp[j] >= p:
                    dp[j + 1] = max(dp[j + 1], dp[j] + l)
                    if dp[j + 1] >= target:
                        result = min(result, j + 1)
                        print(result)
        return result if result < n + 1 else -1