# title: last-stone-weight-ii
# detail: https://leetcode.com/submissions/detail/399762120/
# datetime: Thu Sep 24 02:04:01 2020
# runtime: 76 ms
# memory: 22 MB

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        n = len(stones)
        M = 10 ** 9
        @lru_cache(None)
        def dfs(i, s):
            if i == n:
                return s if s >= 0 else M
            a = dfs(i + 1, s + stones[i])
            b = dfs(i + 1, s - stones[i])
            return min(a, b)
        return dfs(0, 0)