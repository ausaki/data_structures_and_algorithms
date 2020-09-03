# title: time-needed-to-inform-all-employees
# detail: https://leetcode.com/submissions/detail/386079190/
# datetime: Tue Aug 25 16:16:15 2020
# runtime: 1900 ms
# memory: 41.9 MB

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        result = 0
        def inform(i):
            if manager[i] >= 0:
                informTime[i] += inform(manager[i])
                manager[i] = -1
            return informTime[i]
        return max(map(inform, range(n)))