# title: build-array-where-you-can-find-the-maximum-exactly-k-comparisons
# detail: https://leetcode.com/submissions/detail/383614747/
# datetime: Thu Aug 20 15:29:34 2020
# runtime: 1176 ms
# memory: 22.6 MB

class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        MOD = 1000000007
        @lru_cache(None)
        def dp(i, j, k):
            if k == 0:
                return j ** (n - i)
            if (n - i) < k or (m - j) < k:
                return 0
            s1 = sum(dp(i + 1, j, k) for jj in range(1, j + 1)) % MOD
            s2 = sum(dp(i + 1, jj, k - 1) for jj in range(j + 1, m + 1)) % MOD
            return (s1 + s2) % MOD
        return dp(0, 0, k)