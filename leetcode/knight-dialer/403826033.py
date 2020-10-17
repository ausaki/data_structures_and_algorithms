# title: knight-dialer
# detail: https://leetcode.com/submissions/detail/403826033/
# datetime: Sat Oct  3 15:49:20 2020
# runtime: 1448 ms
# memory: 14.1 MB

class Solution:
    def knightDialer(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        jump = [[4, 6], [6, 8], [7, 9], [4, 8], [3, 9, 0], [], [0, 1, 7], [2, 6], [1, 3], [2, 4]]
        dp = [1] * 10
        for i in range(1, n):
            new = [0] * 10
            for j in range(10):
                new[j] = sum(dp[k] for k in jump[j]) % MOD
            dp = new
        return sum(dp) % MOD
