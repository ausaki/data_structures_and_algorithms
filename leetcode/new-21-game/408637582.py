# title: new-21-game
# detail: https://leetcode.com/submissions/detail/408637582/
# datetime: Wed Oct 14 21:22:29 2020
# runtime: 108 ms
# memory: 14.5 MB

class Solution:
    def new21Game(self, N: int, K: int, W: int) -> float:
        dp = collections.deque([0] * W)
        s = 0
        for i in range(W):
            dp[i] = 1 if K + i <= N else 0
            s += dp[i]
        for i in range(K - 1, -1, -1):
            dp.appendleft(s / W)
            s += dp[0] - dp.pop()
        return dp[0]