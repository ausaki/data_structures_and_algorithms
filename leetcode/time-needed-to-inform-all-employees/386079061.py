# title: time-needed-to-inform-all-employees
# detail: https://leetcode.com/submissions/detail/386079061/
# datetime: Tue Aug 25 16:15:46 2020
# runtime: 2052 ms
# memory: 41.9 MB

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        result = 0
        def inform(i):
            if manager[i] >= 0:
                informTime[i] += inform(manager[i])
                manager[i] = -1
            return informTime[i]
        for i in range(n):
            result = max(result, inform(i))
        return result