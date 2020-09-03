# title: time-needed-to-inform-all-employees
# detail: https://leetcode.com/submissions/detail/386069823/
# datetime: Tue Aug 25 15:45:33 2020
# runtime: 2488 ms
# memory: 53.2 MB

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        t = collections.defaultdict(list)
        for i, j in enumerate(manager):
            t[j].append(i)
        def inform(i):
            if i not in t:
                return 0
            return informTime[i] + max(inform(j) for j in t[i])
        return inform(headID)