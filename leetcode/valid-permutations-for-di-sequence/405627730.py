# title: valid-permutations-for-di-sequence
# detail: https://leetcode.com/submissions/detail/405627730/
# datetime: Wed Oct  7 16:13:58 2020
# runtime: 92 ms
# memory: 23 MB

from functools import lru_cache

class Solution:
    def numPermsDISequence(self, S):
        MOD = 10**9 + 7
        N = len(S)

        @lru_cache(None)
        def dp(i, j):
            # How many ways to place P_i with relative rank j?
            if not (0 <= j <= i):
                return 0
            if i == 0:
                return 1
            elif S[i-1] == 'D':
                return (dp(i - 1, j) + dp(i, j + 1)) % MOD
            else:
                return (dp(i-1, j - 1) + dp(i, j - 1)) % MOD

        return sum(dp(N, j) for j in range(N+1)) % MOD