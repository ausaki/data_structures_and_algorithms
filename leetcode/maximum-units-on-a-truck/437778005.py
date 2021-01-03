# title: maximum-units-on-a-truck
# detail: https://leetcode.com/submissions/detail/437778005/
# datetime: Sun Jan  3 10:34:56 2021
# runtime: 172 ms
# memory: 14.6 MB

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda k: k[1], reverse=True)
        res = 0
        for i, j in boxTypes:
            m = min(i, truckSize)
            res += m * j
            truckSize -= m
            if truckSize <= 0:
                break
        return res