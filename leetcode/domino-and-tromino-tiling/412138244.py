# title: domino-and-tromino-tiling
# detail: https://leetcode.com/submissions/detail/412138244/
# datetime: Fri Oct 23 12:56:27 2020
# runtime: 28 ms
# memory: 14.3 MB

class Solution:
    MOD = 10 ** 9 + 7
    dp = [1, 1]
    prefix = [1, 2]
    
    def numTilings(self, N: int) -> int:
        for i in range(len(self.dp), N + 1):
            cnt = self.prefix[-1] * 2 - self.dp[-2] - self.dp[-1]
            cnt %= self.MOD
            self.dp.append(cnt)
            self.prefix.append(self.prefix[-1] + cnt)
        return self.dp[N]