# title: maximize-grid-happiness
# detail: https://leetcode.com/submissions/detail/420818983/
# datetime: Mon Nov 16 16:28:34 2020
# runtime: 1456 ms
# memory: 177.4 MB

class Solution:
    def getMaxGridHappiness(self, m: int, n: int, introvertsCount: int, extrovertsCount: int) -> int:
        @lru_cache(None)
        def dp(i, j, top, it, et):
            if j == n:
                return dp(i + 1, 0, top, it, et)
            if i == m:
                return 0
            if it == 0 and et == 0:
                return 0
            mask = ~(3 << (j * 2))
            ans = dp(i, j + 1, top & mask, it, et)
            l = top >> (2 * (j - 1)) & 3 if j else 0
            t = top >> (2 * j) & 3  
            if it:
                h = 120
                if l == 1:
                    h -= 60
                elif l == 2:
                    h -= 10
                if t == 1:
                    h -= 60
                elif t == 2:
                    h -= 10
                ans = max(ans, h + dp(i, j + 1, top & mask | (1 << (2 * j)), it - 1, et))
            if et:
                h = 40
                if l == 1:
                    h -= 10
                elif l == 2:
                    h += 40
                if t == 1:
                    h -= 10
                elif t == 2:
                    h += 40
                ans = max(ans, h + dp(i, j + 1, top & mask | (2 << (2 * j)), it, et - 1))
            return ans
        
        return dp(0, 0, 0, introvertsCount, extrovertsCount)