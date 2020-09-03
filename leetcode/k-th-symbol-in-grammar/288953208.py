# title: k-th-symbol-in-grammar
# detail: https://leetcode.com/submissions/detail/288953208/
# datetime: Fri Dec 27 20:43:25 2019
# runtime: 28 ms
# memory: 12.7 MB

class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        def find(n, k):
            if n == 1:
                return 0
            i = find(n - 1, (k + 1) // 2)
            if i == 0:
                return 0 if k % 2 else 1
            return 1 if k % 2 else 0
        return find(N, K)