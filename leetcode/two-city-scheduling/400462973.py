# title: two-city-scheduling
# detail: https://leetcode.com/submissions/detail/400462973/
# datetime: Fri Sep 25 14:59:09 2020
# runtime: 36 ms
# memory: 14.2 MB

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        m = n // 2
        a = sum(i for i, j in costs)
        return a + sum(heapq.nsmallest(m, [j - i for i, j in costs]))
                            