# title: minimum-cost-to-merge-stones
# detail: https://leetcode.com/submissions/detail/401417852/
# datetime: Sun Sep 27 23:21:38 2020
# runtime: 52 ms
# memory: 14.7 MB

class Solution:
    def mergeStones(self, stones: List[int], K: int) -> int:
        n = len(stones)
        if n == 1: return 0
        if n == K: return sum(stones)
        if K > n or (K > 2 and n % (K - 1) != 1): return -1
        M = 10 ** 9
        @lru_cache(None)
        def dfs(i, j, k):
            if (j - i + 1 - k) % (K - 1):
                return M
            if i == j:
                return 0 if k == 1 else M
            if k == 1:
                return sum(stones[i:j + 1]) + dfs(i, j, K)
            cost = M
            for l in range(i, j, K - 1):
                cost = min(cost, dfs(i, l, 1) + dfs(l + 1, j, k - 1))
            return cost
        return dfs(0, n - 1, 1)