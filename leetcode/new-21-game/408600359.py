# title: new-21-game
# detail: https://leetcode.com/submissions/detail/408600359/
# datetime: Wed Oct 14 18:18:33 2020
# runtime: 252 ms
# memory: 32.3 MB

class Solution:
    def new21Game(self, N: int, K: int, W: int) -> float:
        @lru_cache(None)
        def dp(k):
            if k <= 0:
                return 1 if -k + K <= N else 0
            if k == 1:
                return sum(dp(k - i) for i in range(1, W + 1)) / W
            a = dp(k - 1)
            c = dp(k - W - 1)
            a = a / W + a - c / W
            return a
        a = dp(K)
        return a