# title: domino-and-tromino-tiling
# detail: https://leetcode.com/submissions/detail/412167612/
# datetime: Fri Oct 23 14:30:10 2020
# runtime: 32 ms
# memory: 14 MB

class Solution:
    MOD = 10 ** 9 + 7
    dp = [1, 1, 2]
    
    def numTilings(self, N: int) -> int:
        for i in range(len(self.dp), N + 1):
            self.dp.append((2 * self.dp[-1] + self.dp[-3]) % self.MOD)
        return self.dp[N]