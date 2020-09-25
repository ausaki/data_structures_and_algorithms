# title: minimum-cost-to-connect-two-groups-of-points
# detail: https://leetcode.com/submissions/detail/399219378/
# datetime: Tue Sep 22 22:26:02 2020
# runtime: 9556 ms
# memory: 35.3 MB

class Solution:
    def connectTwoGroups(self, cost: List[List[int]]) -> int:
        m, n = len(cost), len(cost[0])
        rows = [0] * m
        cols = [0] * n
        result = 0
        for i in range(m):
            c = 0
            for j in range(n):
                if cost[i][j] < cost[i][c]:
                    c = j
            rows[i] = c
            cols[c] += 1
            result += cost[i][c]
        if cols.count(0) == 0:
            return result
        cache = [collections.Counter() for i in range(m)]
        s = (1 << n) - 1
        s0 = s
        while s0:
            c = 0
            for i in range(m):
                for k in range(n):
                    if (1 << k) & s0:
                        cache[i][s0] += cost[i][k]
            s0 = (s0 - 1) & s
        M = 10 ** 9
        @lru_cache(None)
        def dfs(i, j):
            if i == m:
                if bin(j).count('1') == n:
                    return 0
                return M
            result = M
            result = min(result, min((cost[i][k] for k in range(n) if (1 << k) & j), default=M) + dfs(i + 1, j))
            s = ~j & ((1 << n) - 1)
            s0 = s
            while s0:
                result = min(result, cache[i][s0] + dfs(i + 1, j | s0))
                s0 = (s0 - 1) & s
            return result            
        result = dfs(0, 0)
        return result