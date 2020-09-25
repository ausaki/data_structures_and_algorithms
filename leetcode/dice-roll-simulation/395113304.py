# title: dice-roll-simulation
# detail: https://leetcode.com/submissions/detail/395113304/
# datetime: Sun Sep 13 22:56:56 2020
# runtime: 116 ms
# memory: 14 MB

class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        MOD = 10 ** 9 + 7
        dp =collections.deque([[1] * 6 for i in range(16)])
        for i in range(2,  n + 1):
            dp2 = [0]  * 6
            for j in range(6):
                if i - rollMax[j] <= 0:
                    dp2[j] = sum(dp[-1]) % MOD
                elif i - rollMax[j] == 1:
                    dp2[j] = (sum(dp[-1]) - 1) % MOD
                else:
                    p = dp[-rollMax[j] - 1]
                    dp2[j] = (sum(dp[-1]) - sum(p) + p[j]) % MOD
            dp.popleft()
            dp.append(dp2)
        return sum(dp[-1]) % MOD
