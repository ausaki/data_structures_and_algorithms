# title: dice-roll-simulation
# detail: https://leetcode.com/submissions/detail/395048622/
# datetime: Sun Sep 13 18:53:07 2020
# runtime: 1320 ms
# memory: 13.6 MB

class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        MOD = 10 ** 9 + 7
        dp =collections.deque([[0] * 7 for i in range(max(rollMax))])
        dp[0] = [1] * 7
        for i in range(1,  n + 1):
            dp2 = [0]  * 7
            for j in range(7):
                for d in range(6):
                    if d == j:
                        continue
                    for k in range(min(rollMax[d], i)):
                        dp2[j] = (dp2[j] + dp[k][d]) % MOD
            dp.pop()
            dp.appendleft(dp2)
        # print(dp)
        return dp[0][6] % MOD
#         @lru_cache(None)
#         def roll(j, i):
#             if i == 0:
#                 return 1
#             cnt = 0
#             for d in range(6):
#                 if d != j:
#                     for k in range(min(rollMax[d], i)):
#                         cnt = (cnt + roll(d, i - k - 1)) % MOD
#             return cnt
        
#         return roll(-1, n)