# title: domino-and-tromino-tiling
# detail: https://leetcode.com/submissions/detail/412134305/
# datetime: Fri Oct 23 12:43:43 2020
# runtime: 1128 ms
# memory: 16 MB

class Solution:
    MOD = 10 ** 9 + 7
    
    @lru_cache(None)
    def numTilings(self, N: int) -> int:
        if N == 0:
            return 1
        cnt = 0
        for i in range(N):
            j = self.numTilings(i)
            if i < N - 2:
                j *= 2
            cnt = (cnt + j) % self.MOD
        return cnt