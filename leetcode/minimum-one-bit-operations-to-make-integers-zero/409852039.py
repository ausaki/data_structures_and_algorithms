# title: minimum-one-bit-operations-to-make-integers-zero
# detail: https://leetcode.com/submissions/detail/409852039/
# datetime: Sat Oct 17 23:34:34 2020
# runtime: 40 ms
# memory: 14.3 MB

class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        if n == 0:
            return 0
        m = n.bit_length()
        return (1 << m) - 1 - self.minimumOneBitOperations(n & ((1 << (m - 1)) - 1))
        
        
        