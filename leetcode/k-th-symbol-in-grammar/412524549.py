# title: k-th-symbol-in-grammar
# detail: https://leetcode.com/submissions/detail/412524549/
# datetime: Sat Oct 24 16:02:07 2020
# runtime: 32 ms
# memory: 14 MB

class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        if N == 1:
            return 0
        b = self.kthGrammar(N - 1, (K + 1) // 2)
        return b if K % 2 else (b + 1) % 2
