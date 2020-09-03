# title: elimination-game
# detail: https://leetcode.com/submissions/detail/365996335/
# datetime: Mon Jul 13 18:50:53 2020
# runtime: 52 ms
# memory: 13.7 MB

class Solution:
    def lastRemaining(self, n: int) -> int:
        return (2 * (n // 2 - self.lastRemaining(n // 2) + 1)) if n > 1 else 1
            