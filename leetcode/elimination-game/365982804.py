# title: elimination-game
# detail: https://leetcode.com/submissions/detail/365982804/
# datetime: Mon Jul 13 17:49:04 2020
# runtime: 92 ms
# memory: 13.7 MB

class Solution:
    def lastRemaining(self, n: int) -> int:
        if n == 1:
            return 1
        n //= 2
        return 2 * (n - self.lastRemaining(n) + 1)
            