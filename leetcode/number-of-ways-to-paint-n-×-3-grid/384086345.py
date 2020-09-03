# title: number-of-ways-to-paint-n-×-3-grid
# detail: https://leetcode.com/submissions/detail/384086345/
# datetime: Fri Aug 21 15:06:21 2020
# runtime: 52 ms
# memory: 13.6 MB

class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        if n == 1:
            return 12
        n -= 2
        a = b = 1
        while n:
            b = 2 * (a + b) % MOD
            a = (a + b) % MOD
            n -= 1
        return 6 * (a * 5 + b * 4) % MOD