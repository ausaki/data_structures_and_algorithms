# title: minimum-one-bit-operations-to-make-integers-zero
# detail: https://leetcode.com/submissions/detail/409851485/
# datetime: Sat Oct 17 23:33:15 2020
# runtime: 24 ms
# memory: 14.1 MB

class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        if n == 0:
            return 0
        m = n.bit_length()
        steps = (1 << m) - 1
        n = n & ((1 << (m - 1)) - 1)
        return steps - self.minimumOneBitOperations(n)
        
        
        