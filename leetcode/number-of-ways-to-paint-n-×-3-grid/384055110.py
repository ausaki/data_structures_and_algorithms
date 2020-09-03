# title: number-of-ways-to-paint-n-×-3-grid
# detail: https://leetcode.com/submissions/detail/384055110/
# datetime: Fri Aug 21 13:43:27 2020
# runtime: 3788 ms
# memory: 496.9 MB

class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        @lru_cache(None)
        def paint(i, j, color):
            if i == n:
                return 1
            if j == 3:
                return paint(i + 1, 0, color)
            u = (color >> (2 * j)) & 3
            l = (color >> (2 * (j - 1))) & 3 if j >= 1 else 0
            cnt = 0
            for c in range(1, 4):
                if c == u or c == l:
                    continue
                cnt = (cnt + paint(i, j + 1, ~(3 << (2 * j)) & color | (c << (2 * j)))) % MOD
            return cnt
        
        return paint(0, 0, 0)