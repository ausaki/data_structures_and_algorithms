# title: knight-dialer
# detail: https://leetcode.com/submissions/detail/403838836/
# datetime: Sat Oct  3 16:35:57 2020
# runtime: 56 ms
# memory: 15.8 MB

class Solution:
    dp = [[1] * 10]
    def knightDialer(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        jump = [[4, 6], [6, 8], [7, 9], [4, 8], [3, 9, 0], [], [0, 1, 7], [2, 6], [1, 3], [2, 4]]
        for i in range(len(self.dp), n):
            new = [0] * 10
            for j in range(10):
                new[j] = sum(self.dp[-1][k] for k in jump[j]) % MOD
            self.dp.append(new)
        return sum(self.dp[n - 1]) % MOD
