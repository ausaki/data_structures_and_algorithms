# title: minimum-one-bit-operations-to-make-integers-zero
# detail: https://leetcode.com/submissions/detail/409851314/
# datetime: Sat Oct 17 23:32:51 2020
# runtime: 32 ms
# memory: 14.5 MB

class Solution:
    @lru_cache(None)
    def minimumOneBitOperations(self, n: int) -> int:
        if n == 0:
            return 0
        m = n.bit_length()
        steps = (1 << m) - 1
        n = n & ((1 << (m - 1)) - 1)
        return steps - self.minimumOneBitOperations(n)
        
        
        