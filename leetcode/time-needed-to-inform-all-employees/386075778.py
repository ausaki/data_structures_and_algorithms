# title: time-needed-to-inform-all-employees
# detail: https://leetcode.com/submissions/detail/386075778/
# datetime: Tue Aug 25 16:04:49 2020
# runtime: 1192 ms
# memory: 41.6 MB

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        def helper(emp):
            if manager[emp]>=0:
                informTime[emp]+=helper(manager[emp])
                manager[emp]= -1
            return informTime[emp]
        return max(map(helper,manager))