# title: k-th-symbol-in-grammar
# detail: https://leetcode.com/submissions/detail/412526287/
# datetime: Sat Oct 24 16:10:22 2020
# runtime: 32 ms
# memory: 14.1 MB

class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        if N == 1:
            return 0
        return self.kthGrammar(N - 1, (K + 1) // 2) ^ (K & 1) ^ 1
