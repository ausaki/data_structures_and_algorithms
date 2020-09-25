# title: dice-roll-simulation
# detail: https://leetcode.com/submissions/detail/395039280/
# datetime: Sun Sep 13 18:15:10 2020
# runtime: 1408 ms
# memory: 29.6 MB

class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        MOD = 10 ** 9 + 7
        @lru_cache(None)
        def roll(j, i):
            if i == 0:
                return 1
            if i < 0:
                return 0
            cnt = 0
            for d in range(6):
                if d != j:
                    for k in range(rollMax[d]):
                        cnt = (cnt + roll(d, i - k - 1)) % MOD
            return cnt
        
        return roll(-1, n)