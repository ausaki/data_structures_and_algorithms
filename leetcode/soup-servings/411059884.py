# title: soup-servings
# detail: https://leetcode.com/submissions/detail/411059884/
# datetime: Tue Oct 20 21:50:23 2020
# runtime: 44 ms
# memory: 15.8 MB

class Solution:
    @lru_cache(None)
    def dp(self, a, b):
        if a <= 0:
            return 0.5 if b <= 0 else 1
        if b <= 0:
            return 0
        return 0.25 * (self.dp(a - 4, b) + self.dp(a - 3, b - 1) + self.dp(a - 2, b - 2) + self.dp(a - 1, b - 3))
        
    def soupServings(self, N: int) -> float:
        n = (N + 24) // 25
        if n >= 500:
            return 1
        return self.dp(n, n)