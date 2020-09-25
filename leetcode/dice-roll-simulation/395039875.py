# title: dice-roll-simulation
# detail: https://leetcode.com/submissions/detail/395039875/
# datetime: Sun Sep 13 18:17:24 2020
# runtime: 1492 ms
# memory: 29.7 MB

class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        MOD = 10 ** 9 + 7
        @lru_cache(None)
        def roll(j, i):
            if i == 0:
                return 1
            cnt = 0
            for d in range(6):
                if d != j:
                    for k in range(min(rollMax[d], i)):
                        cnt = (cnt + roll(d, i - k - 1)) % MOD
            return cnt
        
        return roll(-1, n)