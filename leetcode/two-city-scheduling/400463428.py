# title: two-city-scheduling
# detail: https://leetcode.com/submissions/detail/400463428/
# datetime: Fri Sep 25 15:00:37 2020
# runtime: 32 ms
# memory: 14.1 MB

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        return sum(i for i, j in costs) + sum(heapq.nsmallest(len(costs) // 2, (j - i for i, j in costs)))
                            