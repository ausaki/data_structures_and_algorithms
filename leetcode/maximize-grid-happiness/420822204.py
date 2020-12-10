# title: maximize-grid-happiness
# detail: https://leetcode.com/submissions/detail/420822204/
# datetime: Mon Nov 16 16:41:08 2020
# runtime: 1584 ms
# memory: 130.3 MB

class Solution:
    def getMaxGridHappiness(self, m: int, n: int, introvertsCount: int, extrovertsCount: int) -> int:
        @lru_cache(None)
        def dp(pos, top, people):
            i, j = divmod(pos, n)
            if i == m:
                return 0
            if people == 0:
                return 0
            mask = ~(3 << (j * 2))
            ans = dp(pos + 1, top & mask, people)
            l = top >> (2 * (j - 1)) & 3 if j else 0
            t = top >> (2 * j) & 3
            it, et = people & 7, people >> 3 & 7
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
                ans = max(ans, h + dp(pos + 1, top & mask | (1 << (2 * j)), et << 3 | it - 1))
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
                ans = max(ans, h + dp(pos + 1, top & mask | (2 << (2 * j)), (et - 1) << 3 | it))
            return ans
        
        return dp(0, 0, extrovertsCount << 3 | introvertsCount)