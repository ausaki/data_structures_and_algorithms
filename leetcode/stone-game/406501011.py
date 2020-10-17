# title: stone-game
# detail: https://leetcode.com/submissions/detail/406501011/
# datetime: Fri Oct  9 16:34:38 2020
# runtime: 360 ms
# memory: 14.3 MB

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        prefix = [0]
        for p in piles:
            prefix.append(prefix[-1] + p)
        n = len(piles)
        dp = [0] * n
        dp[n - 1] = piles[n - 1]
        for i in range(n - 2, -1, -1):
            for j in range(i, n):
                a = piles[i] + prefix[j + 1] - prefix[i + 1] - dp[j]
                b = piles[j] + prefix[j] - prefix[i] - dp[j - 1]
                dp[j] = max(a, b)
        return dp[n - 1] > prefix[-1] // 2