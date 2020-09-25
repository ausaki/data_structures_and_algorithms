# title: stone-game-ii
# detail: https://leetcode.com/submissions/detail/397009334/
# datetime: Thu Sep 17 19:59:55 2020
# runtime: 68 ms
# memory: 14.7 MB

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        @lru_cache(None)
        def dp(i, m):
            if i == n:
                return 0, 0
            if 2 * m >= n - i:
                return sum(piles[i:]), 0
            s = 0
            a, b = 0, 10 ** 8
            for j in range(min(2 * m, n - i)):
                s += piles[i + j]
                c, d = dp(i + j + 1, max(j + 1, m))
                if s + d > a:
                    a = s + d
                    b = c
            return a, b
        return dp(0, 1)[0]
            