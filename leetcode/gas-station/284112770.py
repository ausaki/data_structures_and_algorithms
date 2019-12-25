# title: gas-station
# detail: https://leetcode.com/submissions/detail/284112770/
# datetime: Fri Dec  6 17:40:17 2019
# runtime: 44 ms
# memory: 13.9 MB

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        N = len(gas)
        i = 0
        while i < N:
            print(i)
            g = gas[i] - cost[i]
            j = (i + 1) % N
            while j != i and g >= 0:
                g += gas[j] - cost[j]
                j = (j + 1) % N
            if g >= 0: return i
            if j <= i: break
            i = j
        return -1