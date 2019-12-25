# title: gas-station
# detail: https://leetcode.com/submissions/detail/284116447/
# datetime: Fri Dec  6 18:14:44 2019
# runtime: 48 ms
# memory: 13.8 MB

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total = 0
        tank = 0
        start = 0
        for i, g in enumerate(gas):
            tank += g - cost[i] 
            if tank < 0:
                total += tank
                start = i + 1
                tank = 0
        return -1 if total + tank < 0 else start
                