# title: allocate-mailboxes
# detail: https://leetcode.com/submissions/detail/381102267/
# datetime: Sat Aug 15 14:30:11 2020
# runtime: 540 ms
# memory: 15.8 MB

class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        n = len(houses)
        houses = sorted(houses)
        costs = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                median = houses[(i + j) // 2]
                for t in range(i, j + 1):
                    costs[i][j] += abs(median - houses[t])

        @lru_cache(None)
        def dp(k, i):
            if k == 0 and i == n: return 0
            if k == 0 or i == n: return math.inf
            ans = math.inf
            for j in range(i, n):
                cost = costs[i][j]  # Try to put a mailbox among house[i:j]
                ans = min(ans, cost + dp(k - 1, j + 1))
            return ans

        return dp(k, 0)
        
        
        