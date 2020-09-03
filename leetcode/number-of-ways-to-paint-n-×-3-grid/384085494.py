# title: number-of-ways-to-paint-n-×-3-grid
# detail: https://leetcode.com/submissions/detail/384085494/
# datetime: Fri Aug 21 15:04:15 2020
# runtime: 48 ms
# memory: 14 MB

class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        if n == 1:
            return 12
        n -= 2
        a = b = 1
        while n:
            b = 2 * (a + b) 
            a += b
            n -= 1
        return 6 * (a * 5 + b * 4) % MOD