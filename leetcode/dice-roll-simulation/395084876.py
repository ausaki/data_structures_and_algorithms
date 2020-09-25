# title: dice-roll-simulation
# detail: https://leetcode.com/submissions/detail/395084876/
# datetime: Sun Sep 13 21:21:48 2020
# runtime: 1208 ms
# memory: 13.8 MB

class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        MOD = 10 ** 9 + 7
        dp =collections.deque([[0] * 6 for i in range(max(rollMax))])
        dp[0] = [1] * 6
        for i in range(2,  n + 1):
            dp2 = [0]  * 6
            for j in range(6):
                if rollMax[j] >= i:
                    dp2[j] = 1
                for k in range(min(rollMax[j], i)):
                    for d in range(6):
                        if d == j:
                            continue
                        dp2[j] = (dp2[j] + dp[k][d]) % MOD
            dp.pop()
            dp.appendleft(dp2)
        return sum(dp[0]) % MOD
