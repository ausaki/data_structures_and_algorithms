# title: stone-game
# detail: https://leetcode.com/submissions/detail/406499053/
# datetime: Fri Oct  9 16:26:34 2020
# runtime: 624 ms
# memory: 126.9 MB

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        prefix = [0]
        for p in piles:
            prefix.append(prefix[-1] + p)
        @lru_cache(None)
        def dp(i, j):
            if i == j:
                return piles[i]
            a = piles[i] + prefix[j + 1] - prefix[i + 1] - dp(i + 1, j)
            b = piles[j] + prefix[j] - prefix[i] - dp(i, j - 1)
            return max(a, b)
        return dp(0, len(piles) - 1) > prefix[-1] // 2