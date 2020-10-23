# title: minimum-one-bit-operations-to-make-integers-zero
# detail: https://leetcode.com/submissions/detail/409865147/
# datetime: Sun Oct 18 00:03:45 2020
# runtime: 16 ms
# memory: 14.2 MB

class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        # gray code
        m = 0
        while n:
            m ^= n
            n >>= 1
        return m
        
        
        