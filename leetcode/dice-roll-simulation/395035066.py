# title: dice-roll-simulation
# detail: https://leetcode.com/submissions/detail/395035066/
# datetime: Sun Sep 13 17:57:36 2020
# runtime: 2056 ms
# memory: 192.7 MB

class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        MOD = 10 ** 9 + 7
        @lru_cache(None)
        def roll(i, j, k):
            if i == 0:
                return 1
            cnt = 0 
            for d in range(6):
                if d == j:
                    if k < rollMax[j]:
                        cnt = (cnt + roll(i - 1, d, k + 1)) % MOD
                else:
                    cnt = (cnt + roll(i - 1, d, 1)) % MOD
            return cnt
        
        return roll(n, -1, 0)