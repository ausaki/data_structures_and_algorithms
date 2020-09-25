# title: minimum-cost-to-connect-two-groups-of-points
# detail: https://leetcode.com/submissions/detail/399223843/
# datetime: Tue Sep 22 22:38:36 2020
# runtime: 448 ms
# memory: 21.1 MB

class Solution:
    def connectTwoGroups(self, cost: List[List[int]]) -> int:
        sz1, sz2 = len(cost), len(cost[0])
        min_sz2 = [min([cost[i][j] for i in range(sz1)]) for j in range(sz2)]
        @lru_cache(None)
        def dfs(i: int, mask: int):
            res = 0 if i >= sz1 else float('inf')
            if i >= sz1:
                for j in range(sz2):
                    if mask & (1 << j) == 0:
                        res += min_sz2[j]
            else:
                for j in range(sz2):
                    res = min(res, cost[i][j] + dfs(i + 1, mask | (1 << j)))
            return res
        return dfs(0, 0)