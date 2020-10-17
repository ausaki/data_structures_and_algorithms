# title: number-of-music-playlists
# detail: https://leetcode.com/submissions/detail/404431151/
# datetime: Mon Oct  5 00:28:13 2020
# runtime: 56 ms
# memory: 15.8 MB

class Solution:
    def numMusicPlaylists(self, N: int, L: int, K: int) -> int:
        MOD = 10 ** 9 + 7
        @lru_cache(None)
        def dp(i, j):
            if i < j: return 0
            if i == 0:
                return 1 if j == 0 else 0
            if i == j:
                return (math.factorial(N) // math.factorial(N - j)) % MOD
            a = dp(i - 1, j - 1) * (N - j + 1)
            a += dp(i - 1, j) * (j - K if j > K else 0)
            return a % MOD
        return dp(L, N)
            
            