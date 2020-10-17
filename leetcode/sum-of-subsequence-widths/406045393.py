# title: sum-of-subsequence-widths
# detail: https://leetcode.com/submissions/detail/406045393/
# datetime: Thu Oct  8 14:54:11 2020
# runtime: 300 ms
# memory: 16.5 MB

class Solution:
    def sumSubseqWidths(self, A: List[int]) -> int:
        MOD = 10 ** 9 + 7
        A.sort()
        result = 0
        prev = 0
        powmod = 1
        for i in range(1, len(A)):
            d = A[i] - A[i - 1]
            powmod = (powmod * 2) % MOD
            prev = (2 * prev + d * (powmod - 1)) % MOD
            result = (result + prev) % MOD
        return result