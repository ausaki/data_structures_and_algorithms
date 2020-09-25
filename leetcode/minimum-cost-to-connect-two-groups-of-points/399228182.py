# title: minimum-cost-to-connect-two-groups-of-points
# detail: https://leetcode.com/submissions/detail/399228182/
# datetime: Tue Sep 22 22:50:36 2020
# runtime: 524 ms
# memory: 21.4 MB

class Solution:
    def connectTwoGroups(self, cost: List[List[int]]) -> int:
        m, n = len(cost), len(cost[0])
        min_cols = [101] * n
        cols = [0] * n
        result = 0
        # greedy
        for i in range(m):
            k = 0
            for j in range(n):
                if cost[i][j] < cost[i][k]:
                    k = j
                min_cols[j] = min(min_cols[j], cost[i][j])
            cols[k] += 1
            result += cost[i][k]
        if cols.count(0) == 0:
            return result

        @lru_cache(None)
        def dfs(i, j):
            if i == m:
                c = 0
                for k in range(n):
                    if j & (1 << k) == 0:
                        c += min_cols[k]
                return c
            return min(cost[i][k] + dfs(i + 1, j | (1 << k)) for k in range(n))
        return dfs(0, 0)
