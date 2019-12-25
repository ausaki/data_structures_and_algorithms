# title: integer-replacement
# detail: https://leetcode.com/submissions/detail/279799874/
# datetime: Mon Nov 18 17:27:53 2019
# runtime: 280 ms
# memory: 12.6 MB

class Solution:
    def integerReplacement(self, n: int) -> int:
        if n == 1:
            return 0
        if n & 0x1:
            return 1 + min(self.integerReplacement(n - 1), self.integerReplacement(n + 1))
        return 1 + self.integerReplacement(n >> 1)
            
        